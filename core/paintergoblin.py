#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

from PIL import Image, ImageEnhance

from lib import png
from palettes import palettes


class PainterGoblin:
    def __init__(self):
        """Initialize class by retrieving the palette we're going to work with
        to create a new PainterGoblin Image.
        """
        p = palettes.Palettes()
        self.palette_label, self.palette = p.get_palette()

    def writeimage(self, height, width, pixels, palette, out):
        f = open(out, "wb")
        w = png.Writer(height, width, palette=palette, bitdepth=4)
        w.write(f, pixels)
        f.close()

    def readimage(self, reader, out):
        height, width, pixels, meta = reader.read()
        try:
            _ = meta["palette"]
        except KeyError:
            sys.stderr.write("No palette dictionary returned by PyPNG" + "\n")
            sys.exit(-1)
        self.writeimage(height, width, pixels, self.palette, out)

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
        self.handleimage(
            tmpfolder + "/" + self.tmpfilename, tmpfolder + "/" + outfilename
        )
        os.remove(tmpfolder + "/" + self.tmpfilename)
        return self.palette_label


def paintimage(imagein, imageout):
    # new instance of the painter goblin class...
    pg = PainterGoblin()

    # image palette depth to use...
    depth = 5

    # get an image to paint...
    pg.paintpicture(imagein, depth, "images/", imageout)


def main():

    # 	Usage: 	--img [imgFile]
    # 	Usage: 	--out [imgFile]

    # 	Handle command line arguments for the script
    parser = argparse.ArgumentParser(
        description="Run the Painter Goblin algorithm manually."
    )
    parser.add_argument("--img", help="Image to paint...")
    parser.add_argument(
        "--out", help="OPTIONAL: Output file name...", default="ByThePainterGoblin.png"
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # 	Parse arguments into namespace object to reference later in the script
    global args
    args = parser.parse_args()

    if args.img:
        paintimage(args.img, args.out)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
