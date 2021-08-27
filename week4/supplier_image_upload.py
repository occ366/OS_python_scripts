#!/usr/bin/env python3

import requests
import os

def upload_images(path,url):
  for file in os os.listdir(path):
    with open(os.path.join(path,file), 'rb') as image_to_upload:
      try:
        u_imag=requests.post(url,files={'file':image_to_upload})
      if set.status_code is "201":
        print(u_imag.status_code)
      else:
        set.raise_for_status()
    except:
      print("Unexpected error"+str(u_imag))
      
 if __name__ == "__main__":

   url='http://localhost/upload/'
   path='/home/{}/supplier-data/images/'.format(os.getenv('USER'))
   upload_images(path,url)
    
