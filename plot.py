#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import numpy as np
import argparse
from PIL import Image
from PIL.ExifTags import TAGS

# return focal length of given image
def get_focal_length(img):
    exif = img._getexif()
    if exif is None:
        return

    for id, val in exif.items():
        if TAGS.get(id) == "FocalLength":
            return float(val[0]) / val[1]

# list up files recursively in dir
def find_files(dir = os.curdir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            yield os.path.join(root, file)

# main
parser = argparse.ArgumentParser(description='Plot focal length of JPEG images')
parser.add_argument('source', help='source directory')
args = parser.parse_args()

fl_list = []

for path in find_files(args.source):
    if path.lower().endswith('.jpg'):
        fl = get_focal_length(Image.open(path))
        if fl is None:
            continue
        fl_list.append(fl)

fl_array = np.array(fl_list)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.hist(fl_array, bins=50)
ax.set_xlabel('Focal Length(mm)')
fig.show()
plt.savefig('figure.png')
