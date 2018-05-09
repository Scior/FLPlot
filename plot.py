#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import Image
from PIL.ExifTags import TAGS

def get_focal_length(img):
    exif = img._getexif()
    if exif == None:
        return

    for id, val in exif.items():
        if TAGS.get(id) == "FocalLength":
            return float(val[0]) / val[1]

def find_files(dir = os.curdir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            yield os.path.join(root, file)

for path in find_files():
    if path.endswith('.jpg'):
        print get_focal_length(Image.open(path))
