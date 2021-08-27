#!/usr/bin/env python3

import os
import json
import requests
import sys
import re

def load_json_from_file(path,file):
  """ Read lines of one file and crate a json """
  json_model={"name": 0, "weight": 1, "description":2}
  Json ={}
  with open(os.path.join(path,file)) as f:
    Json_txt=f.readlines()
    for field,position in json_model.items():
      Json[field.strip()]=Json_txt[position].strip('\n')
    Json['image_name']=re.sub('txt','jpeg',file)
  f.close()
  return Json

def api_call(url,Json):
  """ Call the api of one server by url and upload the info of one json """
  headers = {'Content-type': 'application/json'}
  try:
    set=requests.post(url,data=Json,headers=headers)
    if set.status_code is "201":
      print(set.status_code)
    else:
      set.raise_for_status()
  except:
    print("Unexpected error"+str(set.status_code))

if __name__ == "__main__":

  """ main functio: call other fuction for each file we need"""
  ipadd=sys.argv[1]
  path ='/home/{}/supplier-data/descriptions/'.format(os.getenv('USER'))
  url="http://{}/fruits/".format(ipadd)
  for file in os.listdir(path):
    Json=load_json_from_file(path,file)
    w_string = Json["weight"]
    w_int =re.search(r'([\d]*)',w_string)
    Json["weight"]=int(w_int[0])
    api_call(url,json.dumps(Json))
