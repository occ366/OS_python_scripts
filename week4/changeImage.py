#!/usr/bin/env python3
import re
import os
from PIL import Image


def convert_tiff_jpeg(dpath,opath,pattern):
  """convert tiff image to jpge"""
  files = os.listdir(opath)
  for img in files:
   if re.search(pattern,img):
      with Image.open(os.path.join(opath,img)) as im:
        if im.format in "TIFF":
          filename = re.sub('tiff','jpeg',img)
          path =os.path.join(dpath,filename)
          im.resize((600,400)).convert("RGB").save(path,'JPEG')


if __name__ == "__main__":
  USER = os.getenv('USER')
  path = '/home/{}/supplier-data/images/'.format(USER)
  pattern=r'[\w]*.tiff'
  convert_tiff_jpeg(path,path,pattern)
      
  

