#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import urllib
import argparse
from random import seed, shuffle
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
	loc = None
	fileloc = ""
	uri = ""
	arttype = None
	twitter = None

class WikiGoblin:

	#thumbnail query to trial...
	#https://query.wikidata.org/#%23defaultView%3AImageGrid%0ASELECT%20%3Fitem%20%3FitemLabel%20%3Fimage%20%3Floc%20%3FlocLabel%20%3Fcoll%20%3FcollLabel%20%3Fartist%20%3FartistLabel%20%28MD5%28CONCAT%28str%28%3Fitem%29%2Cstr%28RAND%28%29%29%29%29%20as%20%3Frandom%29%20%20WHERE%20%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ125191.%0A%20%20%3Fitem%20wdt%3AP18%20%3Fimage.%0A%20%20OPTIONAL%20%7B%20%3Fitem%20wdt%3AP276%20%3Floc%20.%20%7D%0A%20%20%3Fitem%20wdt%3AP195%20%3Fcoll%20.%0A%20%20%3Fitem%20wdt%3AP170%20%3Fartist%20.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cfr%2Cde%2Cit%22%7D%0A%7D%20ORDER%20BY%20%3Frandom%0ALIMIT%201%0A%0A

	#wikidata types of visual art
	#https://www.wikidata.org/wiki/Wikidata:WikiProject_Visual_arts/Item_structure#Types_of_visual_artworks

	# difficult art styles to work with...
	imgprint = "Q11060274"
	imglitho = "Q15123870"
	imgdrawing = "Q93184"
	imgphoto = "Q125191"

	# good art styles to get a conversion from...
	imgwatercolor = "Q18761202"
	imgpainting = "Q3305213"
	imgwoodcutprint = "Q18219090"
	imgpastel = "Q12043905"
	imgposter = "Q429785"
	imgnone = None

	# art type list...
	arttypes = [imgwatercolor, imgpainting, imgwoodcutprint, imgpastel, imgposter, imgphoto]

	# plain-text art types
	artdict = {imgwatercolor: "#watercolor", imgpainting: "#painting", \
				imgwoodcutprint: "#woodcutprint", imgpastel: "#pastel", \
				imgposter: "#poster", imgphoto: "#photo", imgprint: "#print", \
				imglitho: "#lithograph", imgdrawing: "#drawing"}

	def resultsfromlink(self, link):

		# check we're looking at the URI not the item URL...
		link = link.replace("https://www.wikidata.org/wiki/", "http://www.wikidata.org/entity/")

		sys.stderr.write("retriving from: " + link + "\n")
	
		query = """
		SELECT ?itemLabel ?image ?loc ?locLabel ?coll ?collLabel ?artist ?artistLabel ?twitter_loc ?twitter_coll WHERE {
		  OPTIONAL { <{{LINK}}> rdfs:label ?itemLabel . 
		  FILTER (LANG(?itemLabel) = "en") }
		  <{{LINK}}> wdt:P18 ?image .
  		  OPTIONAL { 
             <{{LINK}}> wdt:P276 ?loc . 
		     ?loc wdt:P2002 ?twitter_loc .
		  }
		  <{{LINK}}> wdt:P195 ?coll .
		  <{{LINK}}> wdt:P170 ?artist .
		  OPTIONAL { ?coll wdt:P2002 ?twitter_coll . }
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,it"}
		}
		LIMIT 1
		"""

		sparql.setQuery(query.replace("{{LINK}}", link))

		sys.stderr.write(query.replace("{{LINK}}", link) + "\n")

		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()

		res = WikiResults()	

		for r in results['results']['bindings']:
			if 'itemLabel' in r:
				res.label = r['itemLabel']['value']
			else:
				res.label = "Untitled"
			res.artist = r['artistLabel']['value']
			if 'locLabel' in r:
				res.loc = r['locLabel']['value']
				if res.loc == "museum's storage space":
					res.loc = r['collLabel']['value']
			if res.loc == None:
				res.loc = r['collLabel']['value']
			res.fileloc = r['image']['value']
			if 'twitter_loc' in r:
				res.twitter = "@" + r['twitter_loc']['value']
			elif 'twitter_coll' in r:
				"twitter col"
				res.twitter = "@" + r['twitter_coll']['value']

		res.uri = link

		return res

	#random query generator from:
	# Partially from https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples
	def newresults(self, style=None, algorithm="MD5"):

		if style is None:
			seed(time.time())
			shuffle(self.arttypes)
			style = self.arttypes[0]

		sys.stderr.write("Painter Goblin is retrieving a " + self.artdict[style] + " to paint... " + "\n")

		query = """
		SELECT ?item ?itemLabel ?image ?loc ?locLabel ?coll ?collLabel ?artist ?artistLabel ?twitter_loc ?twitter_coll ({{ALGORITHM}}(CONCAT(str(?item),str(RAND()))) as ?random)  WHERE {
		  ?item wdt:P31 wd:{{TYPE}}.
		  ?item wdt:P18 ?image.
		  OPTIONAL { 
	         ?item wdt:P276 ?loc . 
			 ?loc wdt:P2002 ?twitter_loc . 
	      }
		  ?item wdt:P195 ?coll .
		  ?item wdt:P170 ?artist .
		  OPTIONAL { ?coll wdt:P2002 ?twitter_coll . }
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,it"}
		} ORDER BY ?random
		LIMIT 1
		"""

		# When we want photos we can use this query...
		photoQuery = """
			#defaultView:ImageGrid
			SELECT ?item ?itemLabel ?image ?loc ?locLabel ?coll ?collLabel ?artist ?artistLabel ?twitter_loc ?twitter_coll ({{ALGORITHM}}(CONCAT(str(?item),str(RAND()))) as ?random)  WHERE {
			  ?item wdt:P31 wd:Q125191.
			  ?item wdt:P18 ?image.
			  OPTIONAL { 
		         ?item wdt:P276 ?loc .
				 ?loc wdt:P2002 ?twitter_loc . 
		      }
			  FILTER NOT EXISTS { ?item wdt:P276 wd:Q666063 . }
			  FILTER NOT EXISTS { ?item wdt:P276 wd:Q2051997 . }
			  ?item wdt:P195 ?coll .
			  ?item wdt:P170 ?artist .
  			  OPTIONAL { ?coll wdt:P2002 ?twitter_coll . }
			  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr,de,it"}
			} ORDER BY ?random
			LIMIT 1
		"""

		query = query.replace("{{ALGORITHM}}", algorithm)
		photoQuery = photoQuery.replace("{{ALGORITHM}}", algorithm)

		if style != self.imgphoto:
			sparql.setQuery(query.replace("{{TYPE}}", style))
			sys.stderr.write(query.replace("{{TYPE}}", style) + "\n")
		else:
			sys.stderr.write(photoQuery + "\n")
			sparql.setQuery(photoQuery)

		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()

		res = WikiResults()	

		for r in results['results']['bindings']:
			res.uri = r['item']['value']
			if 'itemLabel' in r:
				res.label = r['itemLabel']['value']
			else:
				res.label = "Untitled"
			res.artist = r['artistLabel']['value']
			if 'locLabel' in r:
				res.loc = r['locLabel']['value']
				if res.loc == "museum's storage space":
					res.loc = r['collLabel']['value']
			if res.loc == None:
				res.loc = r['collLabel']['value']
			res.fileloc = r['image']['value']
			if 'twitter_loc' in r:
				res.twitter = "@" + r['twitter_loc']['value']
			elif 'twitter_coll' in r:
				"twitter col"
				res.twitter = "@" + r['twitter_coll']['value']	

		res.arttype = self.artdict[style]

		return res

	def getfile(self, res, loc):
		urllib.urlretrieve(res.fileloc, loc)
		return

	# not pretty code below here but works for now... 
	def maketweet(self, res):
		emoji = unicode("🖌🎨", 'utf-8')
		hashtag = "#wikidata #digitalart"
		hashtagshort = "#digitalart"
		urilen = 22
		loc = ""
		arttype = ""

		if res.twitter != None:
			loc = res.twitter
		elif res.loc != None:
			loc = res.loc

		if loc != "" and res.arttype != None:
			tweet = res.label + ", " + res.artist + ", " + loc + " " + res.uri + " " + hashtag + " " + res.arttype + " " + emoji
		elif loc != "" and res.arttype == None:
			tweet = res.label + ", " + res.artist + ", " + loc + " " + res.uri + " " + hashtag + " " + emoji
		elif loc == "" and res.arttype != None:
			tweet = res.label + ", " + res.artist + ", " + res.uri + " " + hashtag + " " + res.arttype + " " + emoji
		else:
			tweet = res.label + ", " + res.artist + ", " + res.uri + " " + hashtag + " " + emoji

		if len(tweet) - urilen + len(emoji) >= 140:
			tweet = tweet.replace(hashtag, hashtagshort)
		else:
			sys.stderr.write("Tweet len, first cut: " + str(len(tweet) - urilen) + "\n")
			return tweet, res.uri

		if len(tweet) - urilen + len(emoji) >= 140:
			tweet = res.label + ", " + res.artist + " " + res.uri + " " + hashtag + " " + emoji
		else:
			sys.stderr.write("Tweet len, first cut: " + str(len(tweet) - urilen) + "\n")
			return tweet, res.uri

		if len(tweet) - urilen + len(emoji) >= 140:
			tweet = res.label + " " + res.uri + " " + hashtag + " " + emoji
		else:
			sys.stderr.write("Tweet len, second cut: " + str(len(tweet) - urilen) + "\n")
			return tweet, res.uri

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

	#not so good styles to generate art from...
	parser.add_argument('--tprint', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tlitho', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tdraw', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tphoto', help='OPTIONAL: Choose an art style to output...', action='store_true')

	#best styles to generate art from...
	parser.add_argument('--twater', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tpaint', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--twood', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tpastel', help='OPTIONAL: Choose an art style to output...', action='store_true')
	parser.add_argument('--tposter', help='OPTIONAL: Choose an art style to output...', action='store_true')

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
	elif args.tdraw:
		style = wg.imgdrawing
	elif args.tphoto:
		style = wg.imgphoto
	elif args.twater:
		style = wg.imgwatercolor
	elif args.tpaint:
		style = wg.imgpainting
	elif args.twood:
		style = wg.imgwoodcutprint
	elif args.tpastel:
		style = wg.imgpastel
	elif args.tposter:
		style = wg.imgposter
	elif args.tlitho:
		style = wg.imglitho

	res = wg.getresults(args.link, style)			
	sys.stdout.write(wg.maketweet(res) + "\n")

if __name__ == "__main__":
	main()

