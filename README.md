# painter-goblin

Painter Goblin Twitter Bot. Inspired by a [Zine](https://github.com/ross-spencer/painter-goblin/tree/master/goblin-zine/pages) I created in 2015.

## Wikidata

Paints new images from Wikidata. The algorithm is simple. Enhance contrast, enhance brightness. This makes muddy images less blurry. Enhance contrast and then convert to paletted image and swap in a randomized curated palette from the collection. 

He enjoys his work, I hope you do!

## Samples

**Die Sterrenag**, Vincent van Gogh, Museum of Modern Art:

![image](samples/01.jpg)

**Liberty Leading the People**, Eugène Delacroix, French paintings, room 77:

![image](samples/02.jpg)

**Macomb's Dam Hotel**, M. A. Sullivan, Metropolitan Museum of Art:

![image](samples/03.jpg)

## Apps

* Paintergoblin.py - creates the images, can be run standalone
* Wikigoblin.py - retrieves data to tweet from the Wikidata SPARQL services
* Twittergoblin.py - Tweets for us! Either a random Wikidata image or from am existing Wikidata link

## License

GPL v3.0
