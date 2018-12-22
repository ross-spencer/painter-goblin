#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import seed, shuffle
from collections import namedtuple


class Palettes:
    def get_palette(self):

        Painter_goblin_palette = namedtuple(
            "Painter_goblin_palette", "label colors"
        )
        p = [
            # france1/seatoun
            Painter_goblin_palette(
                "#Seatoun",
                [
                    (0x00, 0x00, 0x00),
                    (0xFF, 0x00, 0x00),
                    (0xBD, 0xBD, 0xBD),
                    (0x69, 0x78, 0xAD),
                ],
            ),
            # four variants, yellows, reds, blues, greens
            Painter_goblin_palette(
                "#Yellows",
                [
                    (0xEF, 0xEF, 0x3F),
                    (0xC8, 0xC3, 0xC3),
                    (0x3D, 0x3D, 0x3D),
                    (0x53, 0x53, 0x53),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # Reds
            Painter_goblin_palette(
                "#Reds",
                [
                    (0xEF, 0x00, 0x00),
                    (0xC8, 0xC3, 0xC3),
                    (0x3D, 0x3D, 0x3D),
                    (0x53, 0x53, 0x53),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # Greens
            Painter_goblin_palette(
                "#Greens",
                [
                    (0x00, 0xEF, 0x00),
                    (0xC8, 0xC3, 0xC3),
                    (0x3D, 0x3D, 0x3D),
                    (0x53, 0x53, 0x53),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # Blues
            Painter_goblin_palette(
                "#Blues",
                [
                    (0x00, 0x00, 0xEF),
                    (0xC8, 0xC3, 0xC3),
                    (0x1D, 0x1D, 0x1D),
                    (0x53, 0x53, 0x53),
                    (0x00, 0x00, 0xCC),
                ],
            ),
            # madmax
            Painter_goblin_palette(
                "#MadMaxFuryRoad",
                [
                    (0xFB, 0xFD, 0xFA),
                    (0xE3, 0x77, 0x12),
                    (0x1A, 0x37, 0x39),
                    (0x00, 0x64, 0x6C),
                    (0xBB, 0xBB, 0xBB),
                ],
            ),
            # oranges/browns
            Painter_goblin_palette(
                "#OrangeBrowns",
                [
                    (0xC2, 0x8E, 0x27),
                    (0x03, 0x55, 0x52),
                    (0x4D, 0x9C, 0x6D),
                    (0x85, 0x2C, 0x1A),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # magenta, electric green, and others...
            Painter_goblin_palette(
                "#MagentaConverse",
                [
                    (0x00, 0x00, 0x00),
                    (0xFF, 0x53, 0x53),
                    (0xD1, 0xB6, 0xF3),
                    (0xFF, 0x00, 0x69),
                    (0xAA, 0xFF, 0x57),
                ],
            ),
            # rainbow palette
            Painter_goblin_palette(
                unicode("#🌈", "utf-8"),
                [
                    (0x03, 0x03, 0xC1),
                    (0x00, 0xFF, 0x00),
                    (0xFF, 0xFF, 0x00),
                    (0xFF, 0x7F, 0x00),
                    (0xFF, 0x00, 0x00),
                ],
            ),
            # browns and greys
            Painter_goblin_palette(
                "#BrownGrey",
                [
                    (0xC5, 0x7E, 0x42),
                    (0x91, 0x87, 0x8D),
                    (0x7D, 0x70, 0x7C),
                    (0x2A, 0x12, 0x1C),
                    (0x53, 0x6D, 0x81),
                ],
            ),
            # purples and soft greys
            Painter_goblin_palette(
                "#PurpleGrey",
                [
                    (0x81, 0x40, 0x59),
                    (0x55, 0x57, 0x53),
                    (0xD0, 0xCC, 0xCC),
                    (0x2D, 0x31, 0x3D),
                    (0xFE, 0xC4, 0xD0),
                ],
            ),
            # sonic
            Painter_goblin_palette(
                "#SonicTheHedgehog",
                [
                    (0x34, 0x53, 0xCA),
                    (0xFD, 0x92, 0x19),
                    (0x77, 0x98, 0xEE),
                    (0xDF, 0x98, 0x21),
                    (0x68, 0x32, 0x09),
                ],
            ),
            # mario
            Painter_goblin_palette(
                "#SuperMario",
                [
                    (0xEC, 0x4B, 0x09),
                    (0xFF, 0x0A, 0x1A),
                    (0x5D, 0x94, 0xFB),
                    (0x12, 0x7C, 0x22),
                    (0xDB, 0xFC, 0xFF),
                ],
            ),
            # lightblue
            Painter_goblin_palette(
                "#LightBlue",
                [
                    (0x0C, 0x2C, 0x52),
                    (0x5F, 0x6B, 0x61),
                    (0x5E, 0x9D, 0xC8),
                    (0xDC, 0xF0, 0xF7),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # France
            Painter_goblin_palette(
                unicode("#LeTriTricolore 🇫🇷", "utf-8"),
                [(0xFF, 0x00, 0x00), (0xFF, 0xFF, 0xFF), (0x00, 0x00, 0xFF)],
            ),
            # stark
            Painter_goblin_palette(
                "#stark",
                [(0xC0, 0x00, 0x00), (0xFF, 0xFF, 0xFF), (0x00, 0x00, 0x00)],
            ),
            # teletext1 (blue, magenta)
            Painter_goblin_palette(
                "#TeletextBlueMagenta",
                [
                    (0x00, 0xFF, 0xFF),
                    (0x00, 0x00, 0x00),
                    (0xFF, 0x00, 0x00),
                    (0xFF, 0x00, 0xFF),
                ],
            ),
            # teletext2 (yellow, green, blue)
            Painter_goblin_palette(
                "#TeletextYellowGreenBlue",
                [
                    (0xFE, 0xFE, 0x00),
                    (0x00, 0xFE, 0xFE),
                    (0x00, 0xFE, 0x00),
                    (0xFF, 0xFF, 0xFF),
                ],
            ),
            # teletext3 (red, yellow blue)
            Painter_goblin_palette(
                "#TeletextRedYellowBlue",
                [
                    (0xFE, 0xFE, 0x00),
                    (0x00, 0xFE, 0xFE),
                    (0xFF, 0x00, 0x00),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # mario sprite
            Painter_goblin_palette(
                "#MarioSprite",
                [
                    (0x3F, 0x47, 0xCC),
                    (0xF9, 0x38, 0x01),
                    (0xFE, 0xA3, 0x46),
                    (0xFF, 0xFF, 0xFF),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # redwhiteblack
            Painter_goblin_palette(
                "#RussianRevolution",
                [
                    (0xDD, 0x00, 0x00),
                    (0xFF, 0xFF, 0xFF),
                    (0x00, 0x00, 0x00),
                    (0xFF, 0xFF, 0xFF),
                    (0xFF, 0xFF, 0xFF),
                ],
            ),
            # bluewhiteblack
            Painter_goblin_palette(
                "#BlueWhiteBlack",
                [
                    (0x0C, 0x2C, 0x52),
                    (0xFF, 0xFF, 0xFF),
                    (0x00, 0x00, 0x00),
                    (0xFF, 0xFF, 0xFF),
                    (0xFF, 0xFF, 0xFF),
                ],
            ),
            # cyan, black, purple, greys...
            Painter_goblin_palette(
                "#CyanBlackPurpleGrey",
                [
                    (0x00, 0x00, 0x00),
                    (0x9C, 0x29, 0xC6),
                    (0xCB, 0xCB, 0xCB),
                    (0x00, 0xD7, 0xCC),
                    (0x61, 0x5E, 0x6A),
                ],
            ),
            # print-test, The Crack, William Kokoni
            Painter_goblin_palette(
                "#WilliamKokoni",
                [
                    (0x00, 0x9D, 0xC4),
                    (0xA0, 0xC3, 0xBD),
                    (0xFA, 0x18, 0x3B),
                    (0x3A, 0x45, 0x42),
                    (0xD6, 0x7B, 0x7E),
                ],
            ),
            # moma, Emigre 29, The Designers Republic, Emigre Inc., Rudy
            # VanderLans, Zuzana Licko, 1994
            Painter_goblin_palette(
                "#Emigre29",
                [
                    (0x50, 0x4D, 0x6B),
                    (0x84, 0x64, 0x5A),
                    (0xA6, 0x9E, 0x9E),
                    (0xFC, 0xC1, 0x78),
                    (0xF6, 0xED, 0xDB),
                ],
            ),
            # toronto queen
            Painter_goblin_palette(
                "#TorontoQueen",
                [
                    (0xFC, 0x2F, 0xAC),
                    (0x00, 0x48, 0xFF),
                    (0x07, 0x1E, 0x45),
                    (0xF0, 0xB3, 0x00),
                    (0xC1, 0xE3, 0xFF),
                ],
            ),
            # warhol cow...
            Painter_goblin_palette(
                "#WarholCow",
                [
                    (0x27, 0x0B, 0x17),
                    (0x7F, 0x0D, 0x34),
                    (0xC8, 0x0F, 0x4E),
                    (0xFE, 0x1D, 0x69),
                    (0xFF, 0xE1, 0x3B),
                ],
            ),
            # palette from wiki image http://www.wikidata.org/entity/Q28771811
            Painter_goblin_palette(
                "#Phoenix",
                [
                    (0xF1, 0xA0, 0x30),
                    (0xF6, 0x59, 0x01),
                    (0xB5, 0x42, 0x19),
                    (0x62, 0x3A, 0x29),
                    (0x2D, 0x28, 0x30),
                ],
            ),
            # alien
            Painter_goblin_palette(
                "#Alien1979",
                [
                    (0x00, 0x02, 0x00),
                    (0x30, 0x5E, 0x1A),
                    (0x77, 0xAC, 0x1A),
                    (0xCE, 0xC3, 0x66),
                    (0xFF, 0xED, 0x21),
                ],
            ),
            # bowie - ziggy stardust
            Painter_goblin_palette(
                "#ZiggyStardust",
                [
                    (0xDF, 0x1C, 0x06),
                    (0x4B, 0x4D, 0x4B),
                    (0x59, 0x55, 0xCC),
                    (0xFF, 0x95, 0x71),
                    (0xFF, 0xEB, 0xDF),
                ],
            ),
            # white, pink
            Painter_goblin_palette(
                "#WhitePink",
                [
                    (0x22, 0x22, 0x22),
                    (0x99, 0x99, 0x99),
                    (0xF8, 0xF8, 0xFF),
                    (0xFE, 0xFE, 0xFA),
                    (0xFF, 0x1F, 0xFA),
                ],
            ),
            # Anna Atkins's cyanotypes:
            # https://digitalcollections.nypl.org/collections/ocean-flowers-anna-atkinss-cyanotypes-of-british-algae#/?tab=navigation
            Painter_goblin_palette(
                "#AnnaAtkins #CyanoTypes",
                [
                    (0x22, 0x67, 0x88),
                    (0x30, 0x6E, 0x8E),
                    (0x59, 0x8C, 0xA6),
                    (0x88, 0xB0, 0xC0),
                    (0xC6, 0xD6, 0xD7),
                ],
            ),
            # velvet underground
            Painter_goblin_palette(
                "#VelvetUnderground",
                [
                    (0xEC, 0xEF, 0xEB),
                    (0xEC, 0xEF, 0xEB),
                    (0xEC, 0xEF, 0xEB),
                    (0xF5, 0xD3, 0x17),
                    (0x00, 0x00, 0x00),
                ],
            ),
            # The Icknield Way, Spencer Gore, 1912
            Painter_goblin_palette(
                "#SpencerGore",
                [
                    (0x95, 0x2B, 0x58),
                    (0x05, 0x6A, 0x47),
                    (0x00, 0x46, 0x76),
                    (0xF7, 0x76, 0x20),
                    (0xFF, 0x9F, 0x22),
                ],
            ),
            # Original Batman
            Painter_goblin_palette(
                "#Batman",
                [(0x39, 0x3A, 0x38), (0xFD, 0xF7, 0x00), (0x00, 0x02, 0x00)],
            ),
            # Picasso: Blue Period: Mother and Child
            Painter_goblin_palette(
                "#PicassoBlue",
                [
                    (0xF4, 0xF4, 0xF4),
                    (0x9B, 0x74, 0x57),
                    (0x3D, 0x64, 0x45),
                    (0x0D, 0x24, 0x46),
                    (0x2B, 0x7A, 0xBC),
                ],
            ),
            # Cybercats
            Painter_goblin_palette(
                "#Cybercats",
                [
                    (0x18, 0x15, 0x13),
                    (0xE1, 0x24, 0x05),
                    (0x57, 0x55, 0x4E),
                    (0x34, 0x91, 0xC6),
                    (0xE7, 0xFF, 0x1E),
                ],
            ),
            # Solaris : Concept Art
            Painter_goblin_palette(
                "#SolarisConcept",
                [
                    (0x10, 0x0E, 0x29),
                    (0xCB, 0xE1, 0x33),
                    (0x30, 0x41, 0x33),
                    (0x30, 0x2E, 0x46),
                    (0xBF, 0x21, 0x3B),
                ],
            ),
            # Leroy W. Flint Apocalypse, A Triptych , c. 1953
            Painter_goblin_palette(
                "#Apocalypse",
                [
                    (0xFF, 0xBB, 0x08),
                    (0xFF, 0x3D, 0x00),
                    (0xB9, 0x00, 0x00),
                    (0x53, 0x00, 0x00),
                    (0x21, 0x02, 0x00),
                ],
            ),
            # kazimir malevich supremus 58
            Painter_goblin_palette(
                "#MalevichSupremus",
                [
                    (0xD2, 0xE2, 0xE0),
                    (0x0C, 0x0C, 0x0C),
                    (0xFF, 0xC3, 0x0D),
                    (0xFF, 0xFF, 0xF1),
                    (0x2A, 0x49, 0x98),
                ],
            ),
            Painter_goblin_palette(
                "#LollyRocket",
                [
                    (0x0E, 0x00, 0x02),
                    (0x31, 0x02, 0x29),
                    (0x5E, 0x00, 0x52),
                    (0xFF, 0x46, 0x42),
                    (0xEB, 0xF6, 0xF9),
                ],
            ),
            Painter_goblin_palette(
                "#KeithHaring",
                [
                    (0x1C, 0x15, 0x09),
                    (0xEB, 0x28, 0x96),
                    (0xFF, 0x74, 0x2B),
                    (0x80, 0xD9, 0x8E),
                    (0xFD, 0xF8, 0x36),
                ],
            ),
            Painter_goblin_palette(
                "#HugoGellert #One",
                [
                    (0x15, 0x0F, 0x12),
                    (0x1E, 0x30, 0x5F),
                    (0xFB, 0x00, 0x00),
                    (0x8F, 0x25, 0x06),
                    (0xFB, 0xCA, 0x09),
                ],
            ),
            Painter_goblin_palette(
                "#HugoGellert #Two",
                [
                    (0x2A, 0x0B, 0x02),
                    (0x15, 0x21, 0x6F),
                    (0xAE, 0x10, 0x03),
                    (0xFF, 0x0C, 0x00),
                    (0xFD, 0xF5, 0xEA),
                ],
            ),
            # Jack Kirby,
            # https://twitter.com/70sscifiart/status/902283302727385088
            Painter_goblin_palette(
                "#KirbyArgo #One",
                [
                    (0x1A, 0x1D, 0x11),
                    (0x4A, 0x31, 0xC8),
                    (0xFC, 0x09, 0x56),
                    (0x00, 0xC1, 0xEE),
                    (0xFF, 0xF6, 0x00),
                ],
            ),
            # Jack Kirby,
            # https://twitter.com/70sscifiart/status/902283302727385088
            Painter_goblin_palette(
                "#KirbyArgo #Two",
                [
                    (0x00, 0x00, 0x00),
                    (0x2D, 0x1D, 0xFF),
                    (0xE8, 0x00, 0x57),
                    (0x00, 0xAC, 0xF4),
                    (0xFB, 0xFE, 0x00),
                ],
            ),
            # Yves Klein
            Painter_goblin_palette(
                unicode("#YvesKlein #Anthropométrie", "utf-8"),
                [
                    (0x11, 0x12, 0x89),
                    (0x06, 0x10, 0xC5),
                    (0x27, 0x25, 0x5D),
                    (0x98, 0x9D, 0xE1),
                    (0xFD, 0xFE, 0xF8),
                ],
            ),
            # Parking Garage
            Painter_goblin_palette(
                "#Unknown #ParkingGarage",
                [
                    (0x83, 0x00, 0x00),
                    (0x00, 0x00, 0x00),
                    (0x00, 0x53, 0x2E),
                    (0xFF, 0x1A, 0x27),
                    (0x00, 0xF4, 0xC8),
                ],
            ),
            # Neukölln / Reuterstrasse
            Painter_goblin_palette(
                unicode("#Neukölln", "utf-8"),
                [
                    (0x33, 0x35, 0x34),
                    (0xED, 0x34, 0x3C),
                    (0x94, 0x8D, 0x7E),
                    (0xDE, 0x81, 0x2A),
                    (0xFF, 0xFF, 0xFF),
                ],
            ),
            # Crypt of Dracula
            Painter_goblin_palette(
                "#CryptOfDracula",
                [
                    (0x12, 0x14, 0x37),
                    (0xAE, 0x00, 0x3D),
                    (0x3C, 0x4B, 0x7E),
                    (0x73, 0x8C, 0xC7),
                    (0xB3, 0xF7, 0xFF),
                ],
            ),
            # Berlin Bahnhof
            Painter_goblin_palette(
                "#Bahnhof",
                [
                    (0x1D, 0x09, 0x00),
                    (0x3E, 0x31, 0x37),
                    (0x9E, 0x27, 0x00),
                    (0xFF, 0x6D, 0x07),
                    (0xC6, 0xBF, 0xB8),
                ],
            ),
            # Berlin Ballet Grafiti
            Painter_goblin_palette(
                "#Ballet",
                [
                    (0x1A, 0x10, 0x0E),
                    (0x61, 0x4D, 0x4A),
                    (0xAF, 0xB7, 0x27),
                    (0x8A, 0xBF, 0xA6),
                    (0xCB, 0xAD, 0xA4),
                ],
            ),
            # Manabe's Psychadelic Cities
            Painter_goblin_palette(
                "#Manabe",
                [
                    (0xD5, 0x2C, 0x7F),
                    (0x5B, 0x8A, 0xD2),
                    (0xF5, 0xE2, 0x83),
                    (0xD0, 0xB0, 0xC5),
                    (0xC0, 0x58, 0x97),
                ],
            ),
            # Wall at the American Museum of Visionary Art featuring the artist
            # Greg Mort's work.
            Painter_goblin_palette(
                "#AmericanVisionary",
                [
                    (0x80, 0x00, 0x00),
                    (0xBA, 0x00, 0x00),
                    (0xE5, 0x00, 0x00),
                    (0xFF, 0x00, 0x00),
                    (0xFF, 0x41, 0x00),
                ],
            ),
            # Purple Rain
            Painter_goblin_palette(
                "#PurpleRain",
                [
                    (0x00, 0x01, 0x02),
                    (0x26, 0x00, 0x84),
                    (0x56, 0x45, 0x6B),
                    (0xff, 0x60, 0xcc),
                    (0xff, 0xdf, 0xd2),
                ],
            ),
            # Frozen (Movie)
            Painter_goblin_palette(
                "#Frozen",
                [
                    (0x00, 0x10, 0x00),
                    (0x6D, 0x34, 0xBA),
                    (0x58, 0x68, 0xFF),
                    (0xd8, 0x61, 0xb4),
                    (0xE5, 0xC2, 0xE5),
                ],
            ),
            # Marie Antoinette (Movie)
            Painter_goblin_palette(
                "#MarieAntoinette #SofiaCoppola",
                [
                    (0xFF, 0x00, 0x3D),
                    (0xFF, 0x6D, 0x86),
                    (0x73, 0x82, 0x87),
                    (0xFF, 0xA4, 0x9D),
                    (0xFF, 0xC9, 0xA3),
                ],
            ),
        ]

        # seed the random number generator
        seed(time.time())

        # get the palette we want
        shuffle(p)

        # get first entry following shuffle
        label = p[0].label
        palette = p[0].colors

        # and shuffle that palette
        shuffle(palette)

        return label, palette
