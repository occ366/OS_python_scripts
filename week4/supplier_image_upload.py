#!/usr/bin/env python3

import requests
import os
import re

def upload_images(path,url):

  for file in os.listdir(path):
    if re.search(r'jpeg',file):
      with open(os.path.join(path,file), 'rb') as image_to_upload:
        try:
          u_imag=requests.post(url,files={'file':image_to_upload})
          if u_imag.status_code is "201":
            print(u_imag.status_code)
          else:
            u_imag.raise_for_status()
        except:
          print("Unexpected error"+str(u_imag))

if __name__ == "__main__":

   url='http://localhost/upload/'
   path='/home/{}/supplier-data/images/'.format(os.getenv('USER'))
   upload_images(path,url)
    
