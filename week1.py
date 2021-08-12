#!/usr/bin/env python3

import os
from PIL import Image

dpath ="/opt/icons/"
opath=""./images"
files = os.listdir(opath)

for img in files:
  if "ic_" in img:
    with image.open(img) as im:
      if im.format in TIFF:
        try:
          conv=im.resize(128,128)
          conv=conv.rotate(90)
          conv=conv.convert("RGB")
          conv.save(join(dpath,img))
        except Exception, e:
          print e
    im.close() 
