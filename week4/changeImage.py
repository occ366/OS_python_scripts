#!/usr/bin/env python3
import re
import os
from PIL import Image


def convert_tiff_jpeg(dpath,opath):
  """convert tiff image to jpge""""
  files = os.listdir(opath)
  for img in files:
   if re.search(pattern,img):
      with Image.open(os.path.join(opath,img)) as im:
        if im.format in "TIFF":
          conv=im.resize((600,400))
          conv=conv.convert("RGB")
          conv.save(os.path.join(dpath,(img+'.jpeg')),'JPEG')
   im.close() 

 def main():
  USER = os.getenv('USER')
  path = '/home/{}/supplier-data/images/'.format(USER)
  convert_tiff_jpeg(path,path):
      
  
main()
