#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib
import argparse
from random import shuffle
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

#wikidata info
#p31, class of
#Q3305213, painting
#p18, image
#p276, location of item
#p170, creator of item

class WikiResults:
	label = ""
	artist = ""
	loc = ""
	fileloc = ""
	uri = ""

class WikiGoblin:

	#thumbnail query to trial...
	#https://query.wikidata.org/#%23defaultView%3AImageGrid%0ASELECT%20%3Fitem%20%3FitemLabel%20%3Fimage%20%3Floc%20%3FlocLabel%20%3Fcoll%20%3FcollLabel%20%3Fartist%20%3FartistLabel%20%28MD5%28CONCAT%28str%28%3Fitem%29%2Cstr%28RAND%28%29%29%29%29%20as%20%3Frandom%29%20%20WHERE%20%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ125191.%0A%20%20%3Fitem%20wdt%3AP18%20%3Fimage.%0A%20%20OPTIONAL%20%7B%20%3Fitem%20wdt%3AP276%20%3Floc%20.%20%7D%0A%20%20%3Fitem%20wdt%3AP195%20%3Fcoll%20.%0A%20%20%3Fitem%20wdt%3AP170%20%3Fartist%20.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cfr%2Cde%2Cit%22%7D%0A%7D%20ORDER%20BY%20%3Frandom%0ALIMIT%201%0A%0A

	#imgprint = "Q11060274"		#a lot of prints seem to be from wales, monitor
	#imgdrawing = "Q93184"
	imgwatercolor = "Q18761202"
	imgpainting = "Q3305213"
	#imgphoto = "Q125191"
	imgnone = None

	arttypes = [imgwatercolor, imgpainting]

	def resultsfromlink(self, link):

		# check we're looking at the URI not the item URL...
		link = link.replace("https://www.wikidata.org/wiki/", "http://www.wikidata.org/entity/")

		sys.stderr.write("retriving from: " + link + "\n")
	
		query = """
		SELECT ?itemLabel ?image ?loc ?locLabel ?coll ?collLabel ?artist ?artistLabel (MD5(CONCAT(str(?item),str(RAND()))) as ?random)  WHERE {
		  <{{LINK}}> rdfs:label ?itemLabel .
		  FILTER (LANG(?itemLabel) = "en") 
		  <{{LINK}}> wdt:P18 ?image .
  		  OPTIONAL { <{{LINK}}> wdt:P276 ?loc . }
		  <{{LINK}}> wdt:P195 ?coll .
		  <{{LINK}}> wdt:P170 ?artist .
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,it"}
		} ORDER BY ?random
		LIMIT 1
		"""

		sparql.setQuery(query.replace("{{LINK}}", link))

		sys.stderr.write(query.replace("{{LINK}}", link) + "\n")

		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()

		res = WikiResults()	

		for r in results['results']['bindings']:
			res.label = r['itemLabel']['value']
			res.artist = r['artistLabel']['value']
			if 'locLabel' in r:
				res.loc = r['locLabel']['value']
				if res.loc == "museum's storage space":
					res.loc = r['collLabel']['value']
			res.fileloc = r['image']['value']

		res.uri = link

		return res

	#random query generator from:
	# Partially from https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples
	def newresults(self, style=None):

		if style is None:
			shuffle(self.arttypes)
			style = self.arttypes[0]

		sys.stderr.write(style + "\n")

		sys.stderr.write("Retrieving new image for the Painter Goblin" + "\n")

		query = """
		SELECT ?item ?itemLabel ?image ?loc ?locLabel ?coll ?collLabel ?artist ?artistLabel (MD5(CONCAT(str(?item),str(RAND()))) as ?random)  WHERE {
		  ?item wdt:P31 wd:{{TYPE}}.
		  ?item wdt:P18 ?image.
		  OPTIONAL { ?item wdt:P276 ?loc . }
		  ?item wdt:P195 ?coll .
		  ?item wdt:P170 ?artist .
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,it"}
		} ORDER BY ?random
		LIMIT 1
		"""

		sparql.setQuery(query.replace("{{TYPE}}", style))
		sys.stderr.write(query.replace("{{TYPE}}", style) + "\n")

		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()

		res = WikiResults()	

		for r in results['results']['bindings']:
			res.uri = r['item']['value']
			res.label = r['itemLabel']['value']
			res.artist = r['artistLabel']['value']
			if 'locLabel' in r:
				res.loc = r['locLabel']['value']
				if res.loc == "museum's storage space":
					res.loc = r['collLabel']['value']
			res.fileloc = r['image']['value']
	
		return res

	def getfile(self, res, loc):
		urllib.urlretrieve(res.fileloc, loc)
		return

	# not pretty code below here but works for now... 
	def maketweet(self, res):
		emoji = unicode("🖌🎨", 'utf-8')
		tweet = res.label + ", " + res.artist + ", " + res.loc + " " + res.uri + " " + emoji
		if len(tweet) >= 140:
			tweet = res.label + ", " + res.artist + " " + res.uri + " " + emoji
		else:
			return tweet
		if len(tweet) >= 140:
			tweet = res.label + " " + res.uri + " " + emoji
		else:
			return tweet

	# get a results structure for our tweet
	def getresults(self, link=False, t=False):
		wg = WikiGoblin()
		if link is not False:
			res = wg.resultsfromlink(link)
		else:	
			res = wg.newresults(t)
		return res

def main():

	#	Usage: 	--link [imgFile]

	#	Handle command line arguments for the script
	parser = argparse.ArgumentParser(description='Run the Wikidata algorithm manually.')
	parser.add_argument('--link', help='OPTIONAL: Wikidata link to retrieve file from...', default=False)
	parser.add_argument('--tprint', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tpaint', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tdraw', help='OPTIONAL: Choose an art style to output...', action='store_true')

	if len(sys.argv)==0:
		parser.print_help()
		sys.exit(1)

	#	Parse arguments into namespace object to reference later in the script
	global args
	args = parser.parse_args()

	wg = WikiGoblin()

	style = wg.imgnone
	if args.tprint:
		style = wg.imgprint
	elif args.tpaint:
		style = wg.imgpainting
	elif args.tdraw:
		style = wg.imgdrawing

	res = wg.getresults(args.link, style)			
	print wg.maketweet(res)

if __name__ == "__main__":
	main()

