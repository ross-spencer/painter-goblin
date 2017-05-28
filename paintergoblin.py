import os
import png
import sys
import argparse
from PIL import Image
from PIL import ImageEnhance
from random import shuffle

class PainterGoblin:

	def writeimage(self, height, width, pixels, palette, out):
		f = open(out, 'wb')
		w = png.Writer(height, width, palette=palette, bitdepth=4)
		w.write(f, pixels)
		f.close()	

	def get_palette(self):
		palette1 = [(0x02,0x01,0x22), (0x02,0x06,0x5D), (0x1B,0x07,0x4D), (0x2B,0x0E,0x76), (0xFF,0xE3,0xDA)]
		palette2 = [(0x00,0x00,0x00), (0xff,0x00,0x00), (0xbd,0xbd,0xbd), (0x69,0x78,0xad)]
		palette3 = [(0xFF,0xF4,0x4F), (0xC8,0xC3,0xC3), (0x3D,0x3D,0x3D), (0x53,0x53,0x53), (0x00,0x00,0x00)]
		palette4 = [(0xFF,0x00,0x00), (0xC8,0xC3,0xC3), (0x3D,0x3D,0x3D), (0x53,0x53,0x53), (0x00,0x00,0x00)]
		palette5 = [(0x00,0xFF,0x00), (0xC8,0xC3,0xC3), (0x3D,0x3D,0x3D), (0x53,0x53,0x53), (0x00,0x00,0x00)]
		palette6 = [(0x00,0x00,0xFF), (0xC8,0xC3,0xC3), (0x3D,0x3D,0x3D), (0x53,0x53,0x53), (0x00,0x00,0x00)]
		palette7 = [(0xfb,0xfd,0xfa), (0xe3,0x77,0x12), (0x1a,0x37,0x39), (0x00,0x64,0x6c), (0xbb,0xbb,0xbb)]
		palette8 = [(0xc2,0x8e,0x27), (0xde,0xdd,0xd8), (0x85,0x2c,0x1a), (0x67,0x91,0x81), (0xb5,0x8f,0x86)]
		palette9 = [(0x00,0x00,0x00), (0xFF,0x53,0x53), (0xd1,0xb6,0xf3), (0xFF,0x00,0x69), (0xaa,0xFF,0x57)]

		p = [palette1, palette2, palette3, palette4, palette5, palette6, palette7, palette8, palette9]

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

	# open the image to convert..
	img = Image.open(imagein)

	# get an image to paint...
	pg.paintpicture(img, depth, "images/", imageout)

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
