#!/usr/bin/env python3
import sys
import os
import json
import requests
from requests import ConnectionError
from requests import HTTPError
from requests import Timeout

json_model={"title":0, "name":1, "date":2, "feedback":3}	 

def load_json_from_file(file):
  """ Read lines of one file and crate a json """
  json ={}
  with open(file) as f:
    json_txt=f.readlines()
    for field,position in json_model-items():
      json[field]=json_txt[position]
  f.close()
  return json

def api_call(url,json):
  """ Call the api of one server by url and upload the info of one json """
  try:
    set=requests.post(url,data=json)
    if set.status_code is "201":
      print(set.text)
    else:
      set.raise_for_status()
    
  except:
    print("Unexpected error "+ str(set))

def main():
  """ main functio: call other fuction for each file we need"""
  path ="./"
  url="http:://"+sys.arg[1]+"/feedback"
  for file in os.listdir(path):
    json=load_json_from_file(file)
    api_call(url,json)

