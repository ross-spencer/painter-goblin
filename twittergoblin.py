# -*- coding: utf-8 -*-

import os
import sys
import argparse
import twitterpieces as tw
from wikigoblin import WikiGoblin
from paintergoblin import PainterGoblin

#legacy
import base64

#twitter
sys.path.insert(0, 'twitter')
from twitter import *

# if the service should stop working, try switching off legacy to 
# modern api... Twitter api difficulties at time of writing when 
# hosted on PythonAnywhere.com...
legacy = False

wg = WikiGoblin()
pg = PainterGoblin()

wikiloc = "images/FromWikiData.jpg"
tempfolder = "images"
paintloc = "PaintedByThePainterGoblin.png"

emoji = unicode("🖌🎨", 'utf-8')


def MakeTweet(link, sendtweet):

	if link is not False:
		res = wg.resultsfromlink(link)
	else:	
		res = wg.newresults()
	
	tweet = wg.maketweet(res)

	wg.getfile(res, wikiloc)

	pg.paintpicture(wikiloc, 5, tempfolder, paintloc)

	tweet = tweet.encode('utf-8')

	sys.stdout.write(tweet + "\n")

	twitter = tw.twitter_authentication()

	if not legacy:

		if sendtweet:
			#update twitter with our image...
			with open(tempfolder + "/" + paintloc, "rb") as imagefile:
				 imagedata = imagefile.read()
			t_upload = tw.twitter_image_authentication()
			imgID = t_upload.media.upload(media=imagedata)["media_id_string"]

			# finally send tweet with the list of media ids:
			twitter.statuses.update(status=tweet, media_ids=imgID)
		else:
			sys.stdout.write("Testing config, Tweet not sent.\n")

	elif legacy:

		if sendtweet:
			with open(tempfolder + "/" + paintloc, "rb") as imagefile:
				 base64_image = base64.b64encode(imagefile.read())

			params = {"media[]": base64_image, "status": tweet, "_base64": True}
			twitter.statuses.update_with_media(**params)

def main():

	#	Usage: 	--link [imgFile]

	#	Handle command line arguments for the script
	parser = argparse.ArgumentParser(description='Run the Wikidata algorithm manually.')
	parser.add_argument('--link', help='OPTIONAL: Wikidata link to retrieve file from...', default=False)
	parser.add_argument('--tweet', help='OPTIONAL: For testing choose not to update Twitter status...', default=True)

	if len(sys.argv)==0:
		parser.print_help()
		sys.exit(1)

	#	Parse arguments into namespace object to reference later in the script
	global args
	args = parser.parse_args()

	if args.tweet != True:
		args.tweet = False

	MakeTweet(args.link, args.tweet)			

if __name__ == "__main__":
	main()

