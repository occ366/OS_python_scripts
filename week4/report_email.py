#!/usr/bin/env python3

import reports
import os
import re
import run
import datetime
import emails

def paragraph(path):
  parag=''
  for file in os.listdir(path):
    data=run.load_json_from_file(path,file)
    parag=parag+("name: {}\nweight: {}\n\n".format(data["name"],data["weight"]))

  return parag

if __name__ == "__main__":
  USER = os.getenv('USER')
  path = '/home/{}/supplier-data/descriptions/'.format(USER)
  attachment ='/tmp/processed.pdf'
  title = 'Process update on'+ str(datetime.date.today().strftime("%B %d, %Y"))
  reports.generate_report(attachment, title, paragraph(path))
  message=emails.generate_email("automation@example.com",
                                "{}@example.com".format(USER),
                                "Upload Completed - Online Fruit Store",
                                "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                                attachment)
  email.send_email(message)

  
