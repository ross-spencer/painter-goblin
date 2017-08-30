# -*- coding: utf-8 -*-

import os
import sys
import argparse
import pylisttopy as pl
import urilist as ulist
import twitterpieces as tw
from wikigoblin import WikiGoblin
from paintergoblin import PainterGoblin
from PIL import Image

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
listloc = "/home/goatslayer/git/ross-spencer/painter-goblin/urilist"

emoji = unicode("🖌🎨", 'utf-8')

def MakeTweet(link, sendtweet, style, algorithm="MD5"):

	if link is not False:
		res = wg.resultsfromlink(link)
	else:	
		res = wg.newresults(style, algorithm)

	# return tuple from maketweet...
	data = wg.maketweet(res)

	# pull apart tuple...
	tweet = data[0]
	uri = data[1]
	
	# unique tweets...
	if not link:
		if uri in ulist.wikilist:
			sys.stderr.write("Painter Goblin has painted this before. Making new Tweet" + "\n")
			return MakeTweet(link, sendtweet, style, "SHA1")		
		else:	
			sys.stderr.write("Adding to Painter Goblin's Tweet list." + "\n")
			ulist.wikilist.append(uri)

	# we've seen attribute error a few times, see if we can
	# counter it here somehow...
	try:
		tweet = tweet.encode('utf-8')
	except AttributeError as e:
		sys.stderr.write(e + "\n")
		return MakeTweet(link, sendtweet, style)

	sys.stderr.write(tweet + "\n")

	wg.getfile(res, wikiloc)
	pg.paintpicture(wikiloc, 5, tempfolder, paintloc)

	#new file
	nf = tempfolder + "/" + paintloc

	#if we need to resize the image, do it here...
	testresize(nf)

	if not legacy:
		if sendtweet:
			sendNewMethod(link, tweet, nf, uri)
	elif legacy:
		if sendtweet:
			sendLegacyMethod(link, tweet, nf, uri)
	else:
		sys.stdout.write("Testing config, Tweet not sent.\n")

def sendNewMethod(link, tweet, nf, uri):
	#update twitter with our image...
	with open(nf, "rb") as imagefile:
		 imagedata = imagefile.read()
	t_upload = tw.twitter_image_authentication()
	imgID = t_upload.media.upload(media=imagedata)["media_id_string"]

	#authenticate at last minute and send...
	try:
		#authenticate and prepare to send tweet...
		twitter = tw.twitter_authentication()
		twitter.statuses.update(status=tweet, media_ids=imgID)
		if not link:
			logtweet(uri)
	except TwitterHTTPError as e:
		sys.stderr.write(e[0] + "\n")
		if "details: {u'errors': [{u'message': u'Internal error', u'code': 131}]}" in e[0]:
			testresize(nf, 0.1)	
			sendNewMethod(link, tweet, nf, uri)

def sendLegacyMethod(link, tweet, nf, uri):
	with open(nf, "rb") as imagefile:
		 base64_image = base64.b64encode(imagefile.read())

	params = {"media[]": base64_image, "status": tweet, "_base64": True}

	#authenticate at last minute and send...
	try:
		#authenticate and prepare to send tweet...
		twitter = tw.twitter_authentication()
		twitter.statuses.update_with_media(**params)
		if not link: 
			logtweet(uri)
	except TwitterHTTPError as e:
		sys.stderr.write(e[0] + "\n")
		if "details: {u'errors': [{u'message': u'Internal error', u'code': 131}]}" in e[0]:
			testresize(nf, 0.1)
		sendLegacyMethod(link, tweet, nf, uri)

def logtweet(wikiuri):
	lto = pl.ListToPy(set(ulist.wikilist), "wikilist", listloc)
	lto.list_to_py()

#filesize needs to be 3145728
def testresize (img, p=None):
	sys.stderr.write("test resize...\n")
	fsz = os.stat(img).st_size
	sys.stderr.write("size: " + str(fsz) + "\n")
	ideal = 1000000
	if p is not None:
		resize(img, float(p))
	elif fsz  >= ideal:
		diff = float(fsz) - float(ideal)
		avg = float(fsz) + float(ideal) / 2
		perc = (diff / avg)
		sys.stderr.write("File size too big, making smaller: " + str(fsz) + "\n")
		sys.stderr.write("Percent too big: " + str(perc * 100) + "\n")
		resize(img, perc)
	else:
		return

def resize(img, perc):
	i = Image.open(img)
	w, h = i.size
	size = int((w-(w*perc)-1)), int((h-(h*perc)-1))
	sys.stderr.write("resize to: " + str(size) + "\n")
	i.thumbnail(size, Image.ANTIALIAS)
	i.save(img, "PNG")
	return testresize(img)

def main():

	#	Usage: 	--link [imgFile]

	#	Handle command line arguments for the script
	parser = argparse.ArgumentParser(description='Run the Wikidata algorithm manually.')
	parser.add_argument('--link', help='OPTIONAL: Wikidata link to retrieve file from...', default=False)
	parser.add_argument('--notweet', help='OPTIONAL: For testing choose not to update Twitter status...', action='store_false')

	#not so good styles to generate art from...
	parser.add_argument('--tprint', help='OPTIONAL: Choose an art style to output...', action='store_true')
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

	MakeTweet(args.link, args.notweet, style)			

if __name__ == "__main__":
	main()

