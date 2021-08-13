#!/usr/bin/env python3
import re
import os
from PIL import Image

def convert_tiff_jpeg(dpath,opath,pattern):
  """convert tiff image to jpge""""
  files = os.listdir(opath)
  for img in files:
   if re.search(pattern,img):
      with Image.open(os.path.join(opath,img)) as im:
        if im.format in "TIFF":
          conv=im.resize((128,128))
          conv=conv.rotate(90)
          conv=conv.convert("RGB")
          conv.save(os.path.join(dpath,img),'JPEG')
   im.close() 

 def main():
  dpath ="/opt/icons/"
  opath="../images"
  pattern =r'ic_'
  convert_tiff_jpeg(dpath,opath,pattern):
      
  
main()
