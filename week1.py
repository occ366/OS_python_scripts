#!/usr/bin/env python3

import os
from PIL import Image

dpath ="/opt/icons/"
opath="../images"


def convert_tiff_jpeg(dpath,opath):
  files = os.listdir(opath)


  for img in files:
   if "ic_" in img:
      with Image.open(os.path.join(opath,img)) as im:
        if im.format in "TIFF":
          conv=im.resize((128,128))
          conv=conv.rotate(90)
          conv=conv.convert("RGB")
           conv.save(os.path.join(dpath,img),'JPEG')
        
   im.close() 

  
  
