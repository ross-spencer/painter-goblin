#!/usr/bin/env bash

SCRIPT_PATH=$(dirname "$0")
IMAGES=$SCRIPT_PATH/images/remix-salon/*

mkdir -p $SCRIPT_PATH/images/low-res/
mkdir -p $SCRIPT_PATH/images/lazy/

if [ -n "$(uname -a | ack Ubuntu)" -a -x "$(command -v mogrify)" ]; then
	for f in $IMAGES
	do
		b=$(basename "${f}")
		fname="${b%.*}"

		# This will convert the source images if needed.
		# gm convert -define webp:lossless=false "${f}" $SCRIPT_PATH/images/remix-salon/"${fname}".webp
		# gm convert "${f}" $SCRIPT_PATH/images/remix-salon/"${fname}".jpg

		gm convert -resize 800x "${f}" $SCRIPT_PATH/images/low-res/"${fname}".min.jpg
		gm convert -resize 32x "${f}" $SCRIPT_PATH/images/lazy/"${fname}".placeholder.jpg
	done
fi

python $SCRIPT_PATH/tools/setup.py
