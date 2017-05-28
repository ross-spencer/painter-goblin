#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib
import argparse
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

	def resultsfromlink(self, link):

		sys.stderr.write("retriving from: " + link + "\n")
	
		string = """
		SELECT ?itemLabel ?image ?loc ?locLabel ?coll ?collLabel ?artist ?artistLabel (MD5(CONCAT(str(?item),str(RAND()))) as ?random)  WHERE {
		  <{{LINK}}> rdfs:label ?itemLabel .
		  <{{LINK}}> wdt:P18 ?image .
		  <{{LINK}}> wdt:P276 ?loc .
		  <{{LINK}}> wdt:P195 ?coll .
		  <{{LINK}}> wdt:P170 ?artist .
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "en"}
		} ORDER BY ?random
		LIMIT 1
		"""

		sparql.setQuery(string.replace("{{LINK}}", link))

		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()

		res = WikiResults()	

		for r in results['results']['bindings']:
			res.label = r['itemLabel']['value']
			res.artist = r['artistLabel']['value']
			res.loc = r['locLabel']['value']
			if res.loc == "museum's storage space":
				res.loc = r['collLabel']['value']
			res.fileloc = r['image']['value']

		res.uri = link

		return res

	#random query generator from:
	# Partially from https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples
	def newresults(self):

		sys.stderr.write("Retrieving new image for the Painter Goblin" + "\n")

		sparql.setQuery("""
		SELECT ?item ?itemLabel ?image ?loc ?locLabel ?coll ?collLabel ?artist ?artistLabel (MD5(CONCAT(str(?item),str(RAND()))) as ?random)  WHERE {
		  ?item wdt:P31 wd:Q3305213.
		  ?item wdt:P18 ?image.
		  ?item wdt:P276 ?loc .
		  ?item wdt:P195 ?coll .
		  ?item wdt:P170 ?artist .
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "en"}
		} ORDER BY ?random
		LIMIT 1
		""")

		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()

		res = WikiResults()	

		for r in results['results']['bindings']:
			res.uri = r['item']['value']
			res.label = r['itemLabel']['value']
			res.artist = r['artistLabel']['value']
			res.loc = r['locLabel']['value']
			if res.loc == "museum's storage space":
				res.loc = r['collLabel']['value']
			res.fileloc = r['image']['value']
	
		return res

	def getfile(self, res, loc):
		urllib.urlretrieve(res.fileloc, loc)

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
	def getresults(self, link=False):
		wg = WikiGoblin()
		if link is not False:
			res = wg.resultsfromlink(link)
		else:	
			res = wg.newresults()
		return res

def main():

	#	Usage: 	--link [imgFile]

	#	Handle command line arguments for the script
	parser = argparse.ArgumentParser(description='Run the Wikidata algorithm manually.')
	parser.add_argument('--link', help='OPTIONAL: Wikidata link to retrieve file from...', default=False)

	if len(sys.argv)==0:
		parser.print_help()
		sys.exit(1)

	#	Parse arguments into namespace object to reference later in the script
	global args
	args = parser.parse_args()

	wg = WikiGoblin()
	res = wg.getresults(args.link)			
	print wg.maketweet(res)

if __name__ == "__main__":
	main()

