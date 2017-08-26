#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import png
import sys
import time
import argparse
from PIL import Image
from PIL import ImageEnhance
from random import seed, shuffle

class PainterGoblin:

	def writeimage(self, height, width, pixels, palette, out):
		f = open(out, 'wb')
		w = png.Writer(height, width, palette=palette, bitdepth=4)
		w.write(f, pixels)
		f.close()	

	def get_palette(self):
		#purple rain
		palette1 = [(0x02,0x01,0x22), (0x02,0x06,0x5D), (0x1B,0x07,0x4D), (0x2B,0x0E,0x76), (0xFF,0xD3,0xCA)]

		#france1/seatoun
		palette2 = [(0x00,0x00,0x00), (0xff,0x00,0x00), (0xbd,0xbd,0xbd), (0x69,0x78,0xad)]

		#four variants, yellows, reds, blues, greens
		palette3 = [(0xEF,0xEF,0x3F), (0xC8,0xC3,0xC3), (0x3D,0x3D,0x3D), (0x53,0x53,0x53), (0x00,0x00,0x00)]
		palette4 = [(0xEF,0x00,0x00), (0xC8,0xC3,0xC3), (0x3D,0x3D,0x3D), (0x53,0x53,0x53), (0x00,0x00,0x00)]
		palette5 = [(0x00,0xEF,0x00), (0xC8,0xC3,0xC3), (0x3D,0x3D,0x3D), (0x53,0x53,0x53), (0x00,0x00,0x00)]
		palette6 = [(0x00,0x00,0xEF), (0xC8,0xC3,0xC3), (0x1D,0x1D,0x1D), (0x53,0x53,0x53), (0x00,0x00,0xCC)]

		#madmax
		palette7 = [(0xfb,0xfd,0xfa), (0xe3,0x77,0x12), (0x1a,0x37,0x39), (0x00,0x64,0x6c), (0xbb,0xbb,0xbb)]

		#oranges/browns
		palette8 = [(0xc2,0x8e,0x27), (0x03,0x55,0x52), (0x4d,0x9c,0x6d), (0x85,0x2c,0x1a), (0x00,0x00,0x00)]

		#magenta, electric green, and others...
		palette9 = [(0x00,0x00,0x00), (0xFF,0x53,0x53), (0xd1,0xb6,0xf3), (0xFF,0x00,0x69), (0xaa,0xFF,0x57)]

		#rainbow palette
		palette10 = [(0x03,0x03,0xc1), (0x00,0xFF,0x00), (0xFF,0xFF,0x00), (0xFF,0x7F,0x00), (0xFF,0x00,0x00)]

		#browns and greys
		palette11 = [(0xc5,0x7e,0x42), (0x91,0x87,0x8d), (0x7d,0x70,0x7c), (0x2a,0x12,0x1c), (0x53,0x6d,0x81)]

		#purples and soft greys
		palette12 = [(0x81,0x40,0x59), (0x55,0x57,0x53), (0xd0,0xcc,0xcc), (0x2d,0x31,0x3d), (0xfe,0xc4,0xd0)]

		#sonic
		palette13 = [(0x34,0x53,0xca),(0xfd,0x92,0x19),(0x77,0x98,0xee),(0xdf,0x98,0x21),(0x68,0x32,0x09)]
		 
		#mario
		palette14 = [(0xec,0x4b,0x09),(0xff,0x0a,0x1a),(0x5d,0x94,0xfb),(0x12,0x7c,0x22),(0xdb,0xfc,0xff)]

		#lightblue
		palette15 = [(0x0c, 0x2c, 0x52), (0x5f, 0x6b, 0x61), (0x5e, 0x9d, 0xc8), (0xdc, 0xf0, 0xf7), (0x00, 0x00, 0x00)]

		#france
		palette16 = [(0xff,0x00,0x00), (0xFF,0xFF,0xFF), (0x00,0x00,0xFF)]

		#stark
		palette17 = [(0xC0,0x00,0x00), (0xFF,0xFF,0xFF), (0x00,0x00,0x00)]

		#teletext1 (blue, magenta)
		palette18 = [(0x00,0xff,0xff),(0x00,0x00,0x00),(0xff,0x00,0x00),(0xff,0x00,0xff)]

		#teletext2 (yellow, green, blue)
		palette19 = [(0xfe,0xfe,0x00),(0x00,0xfe,0xfe),(0x00,0xfe,0x00),(0xff,0xff,0xff)]

		#teletext3 (red, yellow blue)
		palette20 = [(0xfe,0xfe,0x00),(0x00,0xfe,0xfe),(0xff,0x00,0x00),(0x00,0x00,0x00)]

		#mario sprite
		palette21 = [(0x3f,0x47,0xcc),(0xf9,0x38,0x01),(0xfe,0xa3,0x46),(0xFF,0xFF,0xFF),(0x00,0x00,0x00)]

		#redwhiteblack
		palette22 = [(0xdd,0x00,0x00), (0xFF,0xFF,0xFF), (0x00,0x00,0x00), (0xFF,0xFF,0xFF), (0xFF,0xFF,0xFF)]

		#bluewhiteblack
		palette23 = [(0x0c, 0x2c, 0x52), (0xFF,0xFF,0xFF), (0x00,0x00,0x00), (0xFF,0xFF,0xFF), (0xFF,0xFF,0xFF)]

		#cyan, black, purple, greys... 
		palette24 = [(0x00,0x00,0x00), (0x9c,0x29,0xc6), (0xcb,0xcb,0xcb), (0x00,0xd7,0xcc), (0x61,0x5e,0x6a)]

		#print-test, The Crack, William Kokoni
		palette25 = [(0x00,0x9d,0xc4), (0xa0,0xc3,0xbd), (0xfa,0x18,0x3b), (0x3a,0x45,0x42), (0xd6,0x7b,0x7e)]

		#moma, Emigre 29, The Designers Republic, Emigre Inc., Rudy VanderLans, Zuzana Licko, 1994 
		palette26 = [(0x50,0x4d,0x6b),(0x84,0x64,0x5a),(0xa6,0x9e,0x9e),(0xfc,0xc1,0x78),(0xf6,0xed,0xdb)]

		#toronto queen
		palette27 = [(0xfc,0x2f,0xac),(0x00,0x48,0xff),(0x07,0x1e,0x45),(0xf0,0xb3,0x00),(0xc1,0xe3,0xff)]

		#warhol cow... 
		palette28 = [(0x27,0x0b,0x17),(0x7f,0x0d,0x34),(0xc8,0x0f,0x4e),(0xfe,0x1d,0x69),(0xff,0xe1,0x3b)]

		#palette from wiki image http://www.wikidata.org/entity/Q28771811
		palette29 = [(0xf1,0xa0,0x30),(0xf6,0x59,0x01),(0xb5,0x42,0x19),(0x62,0x3a,0x29),(0x2d,0x28,0x30)]

		#alien
		palette30 = [(0x00,0x02,0x00),(0x30,0x5e,0x1a),(0x77,0xac,0x1a),(0xce,0xc3,0x66),(0xff,0xed,0x21)]

		#bowie - ziggy stardust
		palette31 = [(0xdf,0x1c,0x06),(0x4b,0x4d,0x4b),(0x59,0x55,0xcc),(0xff,0x95,0x71),(0xff,0xeb,0xdf)]
		
		#white, pink
		palette32 = [(0xff,0xff,0xff),(0x99,0x99,0x99),(0xf8,0xf8,0xff),(0xfe,0xfe,0xfa),(0xff,0x1f,0xfa)] 

		#white, cyan
		palette33 = [(0xff,0xff,0xff),(0x99,0x99,0x99),(0xf8,0xf8,0xff),(0xfe,0xfe,0xfa),(0x1f,0xff,0xfa)] 

		#white, yellow
		palette34 = [(0xff,0xff,0xff),(0x99,0x99,0x99),(0xf8,0xf8,0xff),(0xfe,0xfe,0xfa),(0xfa,0xff,0x1f)] 

		#The Icknield Way, Spencer Gore, 1912
		palette35 = [(0x95,0x2b,0x58),(0x05,0x6a,0x47),(0x00,0x46,0x76),(0xf7,0x76,0x20),(0xff,0x9f,0x22)]

		#Original Batman
		palette36 = [(0x39,0x3a,0x38),(0xfd,0xf7,0x00),(0x00,0x02,0x00)]

		#Picasso: Blue Period: Mother and Child
		palette37 = [(0xf4,0xf4,0xf4), (0x9b,0x74,0x57), (0x3d,0x64,0x45), (0x0d,0x24,0x46), (0x2b,0x7a,0xbc)]

		p = [palette1, palette2, palette3, palette4, palette5, palette6, palette7, palette8, palette9, \
			palette10, palette11, palette12, palette13, palette14, palette15, palette16, palette17, palette18, \
				palette19, palette20, palette21, palette22, palette23, palette24, palette25, palette26, palette27, \
					palette28, palette29, palette30, palette31, palette32, palette33, palette34, palette35, palette36, palette37]

		#seed the random number generator
		seed(time.time())

		#get the palette we want
		shuffle(p)
	
		#get first entry following shuffle
		p = p[0]

		#and shuffle that palette
		shuffle(p)

		return p

	def readimage(self, reader, out):	
		height, width, pixels, meta = reader.read()
		try:
			palette = meta['palette']
		except KeyError:
			sys.stderr.write("No palette dictionary returned by PyPNG" + "\n")
			sys.exit(-1)
		self.writeimage(height, width, pixels, self.get_palette(), out)

	def handleimage(self, img, out):
		reader = png.Reader(filename=img)
		self.readimage(reader, out)

	def enhance(self, img):
		convert_contrast = ImageEnhance.Contrast(img)
		contrast = convert_contrast.enhance(1.4)
		convert_brightness = ImageEnhance.Brightness(contrast)
		brightness = convert_brightness.enhance(0.9)
		return brightness

	def saturate(self, img):
		s = ImageEnhance.Color(img)
		saturation = s.enhance(1.2)
		return saturation

	def addpalette(self, img, depth):
		return img.convert("P", palette=Image.ADAPTIVE, colors=depth)

	tmpfilename = "enhanced-image.png"

	def paintpicture(self, img, depth, tmpfolder, outfilename):

		# open the image to convert..
		img = Image.open(img)

		i = self.enhance(img)
		i = self.saturate(i)
		i = self.addpalette(i, depth)
		i.save(tmpfolder + "/" + self.tmpfilename, mode="P", colors=depth)
		self.handleimage(tmpfolder + "/" + self.tmpfilename, tmpfolder + "/" + outfilename)
		os.remove(tmpfolder + "/" + self.tmpfilename)

def paintimage(imagein, imageout):
	# new instance of the painter goblin class...
	pg = PainterGoblin()

	# image palette depth to use...
	depth = 5

	# get an image to paint...
	pg.paintpicture(imagein, depth, "images/", imageout)

def main():

	#	Usage: 	--img [imgFile]
	#	Usage: 	--out [imgFile]

	#	Handle command line arguments for the script
	parser = argparse.ArgumentParser(description='Run the Painter Goblin algorithm manually.')
	parser.add_argument('--img', help='Image to paint...')
	parser.add_argument('--out', help='OPTIONAL: Output file name...', default='ByThePainterGoblin.png')

	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)

	#	Parse arguments into namespace object to reference later in the script
	global args
	args = parser.parse_args()

	if args.img:
		paintimage(args.img, args.out)			
	else:
		parser.print_help()
		sys.exit(1)

if __name__ == "__main__":
	main()
