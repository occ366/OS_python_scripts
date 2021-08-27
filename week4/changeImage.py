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
          im.resize((600,400)).convert("RGB").save(os.path.join(dpath,(img+'.jpeg')),'JPEG')

   im.close() 

if __name__ == "__main__":
  USER = os.getenv('USER')
  path = '/home/{}/supplier-data/images/'.format(USER)
  patttern=r'[\w]*.tiff'
  convert_tiff_jpeg(path,path,pattern)
      
  

