#!/usr/bin/env python3

import os
import json
import requests
import sys

def load_json_from_file(path,file):
  """ Read lines of one file and crate a json """
  json_model={"title":0, "name":1, "date":2, "feedback":3}
  Json ={}
  with open(os.path.join(path,file)) as f:
    Json_txt=f.readlines()
    for field,position in json_model.items():
      Json[field.strip()]=Json_txt[position].strip('\n')
  f.close()
  return json.dumps(Json)

def api_call(url,Json):
  """ Call the api of one server by url and upload the info of one json """
  headers = {'Content-type': 'application/json'}
  try:
    payload={'json_payload': Json}
    set=requests.post(url,data=Json,headers=headers)
    if set.status_code is "201":
      print(set.status_code)
    else:
      set.raise_for_status()
  except:
    print("Unexpected error"+str(set))


def main():
  """ main functio: call other fuction for each file we need"""
  ipadd=sys.agrv[1]
  path ="/data/feedback/"
  url="http://{}/feedback/?format=api"´.format(ipadd)
  for file in os.listdir(path):
    json=load_json_from_file(path,file)
    api_call(url,json)

main()
