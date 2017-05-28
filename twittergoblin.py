#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter import *
import os
import sys
import argparse
import twitterpieces as tw
from wikigoblin import WikiGoblin
from paintergoblin import PainterGoblin

#http://www.wikidata.org/entity/Q24204668

wg = WikiGoblin()
pg = PainterGoblin()

wikiloc = "images/FromWikiData.jpg"
tempfolder = "images"
paintloc = "PaintedByThePainterGoblin.png"

def MakeTweet(link):

	if link is not False:
		res = wg.resultsfromlink(link)
	else:	
		res = wg.newresults()
	
	tweet = wg.maketweet(res)

	wg.getfile(res, wikiloc)

	pg.paintpicture(wikiloc, 5, tempfolder, paintloc)

	print tweet

	twitter = tw.twitter_authentication()

	#update twitter with our image...
	with open(tempfolder + "/" + paintloc, "rb") as imagefile:
		 imagedata = imagefile.read()
	t_upload = tw.twitter_image_authentication()
	imgID = t_upload.media.upload(media=imagedata)["media_id_string"]
	# - finally send your tweet with the list of media ids:
	twitter.statuses.update(status=tweet, media_ids=imgID)


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
	MakeTweet(args.link)			

if __name__ == "__main__":
	main()

