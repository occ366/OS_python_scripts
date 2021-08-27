#!/usr/bin/env python3

import json
import locale
import sys
import operator
import os
from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """

  max_revenue = {"revenue": 0}
  sales = {"total_sales": 0}
  best_car = {}
  for item in data:
   # Calculate the revenue generated by this model (price * total_sales)
   # We need to convert the price from "$1234.56" to 1234.56
   item_price = locale.atof(item["price"].strip("$"))
   item_revenue = item["total_sales"] * item_price
   if item_revenue > max_revenue["revenue"]:
     item["revenue"] = item_revenue
     max_revenue = item
   # TODO: also handle max sales
   if item["total_sales"] > sales["total_sales"]:
    sales = item
   # TODO: also handle most popular car_year
   if not item["car"]["car_year"] in best_car.keys():
     best_car[item["car"]["car_year"]] = item["total_sales"]
   else:
     best_car[item["car"]["car_year"]] += item["total_sales"]

   all_values = best_car.values()
   max_value = max(all_values)
   max_key = max(best_car, key=best_car.get)

  summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(format_car(sales["car"]), sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(max_key, max_value),
    ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("../car_sales.json")
  summary = process_data(data)
  print(summary)
  new_summary = '<br/>'.join(summary)
  # TODO: turn this into a PDF report
  report("/tmp/car.pdf", "Sales Summary for last month", new_summary,cars_dict_to_table(data))
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = summary[0]+"\n"+summary[1]+"\n"+summary[2]+"\n"
  message = email_generate(sender, receiver, subject, body, "/tmp/car.pdf")
  email_send(message)

if __name__ == "__main__":
  main(sys.argv)
student-00-80df72c7b64d@linux-instance:~/scripts$ ^C
student-00-80df72c7b64d@linux-instance:~/scripts$ ./cars.py
['The Mercedes-Benz E-Class (2009) generated the most revenue: $22749529.02', 'The Acura Integra (1995) had the most sales: 1192', 'The most popular year was 2007 with 21534 sales.']
You have new mail in /var/mail/student-00-80df72c7b64d
student-00-80df72c7b64d@linux-instance:~/scripts$ sudo nano ./cars.py
You have mail in /var/mail/student-00-80df72c7b64d
student-00-80df72c7b64d@linux-instance:~/scripts$ ./cars.py
['The Mercedes-Benz E-Class (2009) generated the most revenue: $22749529.02', 'The Acura Integra (1995) had the most sales: 1192', 'The most popular year was 2007 with 21534 sales.']
student-00-80df72c7b64d@linux-instance:~/scripts$ sudo nano ./cars.py
You have mail in /var/mail/student-00-80df72c7b64d
student-00-80df72c7b64d@linux-instance:~/scripts$ ./cars.py
['The Mercedes-Benz E-Class (2009) generated the most revenue: $22749529.02', 'The Acura Integra (1995) had the most sales: 1192', 'The most popular year was 2007 with 21534 sales.']
student-00-80df72c7b64d@linux-instance:~/scripts$ sudo nano ./cars.py
student-00-80df72c7b64d@linux-instance:~/scripts$ cat cars.py
#!/usr/bin/env python3

import json
import locale
import sys
import operator
import os
from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """

  max_revenue = {"revenue": 0}
  sales = {"total_sales": 0}
  best_car = {}
  for item in data:
   # Calculate the revenue generated by this model (price * total_sales)
   # We need to convert the price from "$1234.56" to 1234.56
   item_price = locale.atof(item["price"].strip("$"))
   item_revenue = item["total_sales"] * item_price
   if item_revenue > max_revenue["revenue"]:
     item["revenue"] = item_revenue
     max_revenue = item
   # TODO: also handle max sales
   if item["total_sales"] > sales["total_sales"]:
    sales = item
   # TODO: also handle most popular car_year
   if not item["car"]["car_year"] in best_car.keys():
     best_car[item["car"]["car_year"]] = item["total_sales"]
   else:
     best_car[item["car"]["car_year"]] += item["total_sales"]

   all_values = best_car.values()
   max_value = max(all_values)
   max_key = max(best_car, key=best_car.get)

  summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(format_car(sales["car"]), sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(max_key, max_value),
    ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("../car_sales.json")
  summary = process_data(data)
  print(summary)
  new_summary = '<br/>'.join(summary)
  # TODO: turn this into a PDF report
  report("/tmp/car.pdf", "Sales summary for last month", new_summary,cars_dict_to_table(data))
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = new_summary
  message = email_generate(sender, receiver, subject, body, "/tmp/car.pdf")
  email_send(message)

if __name__ == "__main__":
  main(sys.argv)
