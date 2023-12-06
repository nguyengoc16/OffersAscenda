from typing import Any
from urllib import parse
from datetime import datetime, timedelta
import json
import heapq


def render_template(template_name='index.html', context={}):
  html_str = ""
  with open(template_name, 'r') as f:
      html_str = f.read()
      html_str = html_str.format(**context)
  return html_str

def home(environ):
  return render_template(
      template_name='../templates/index.html', 
      context={}).encode("utf-8")

def not_found(environ, path):
  return render_template(template_name='../templates/404.html', context={"path": path}).encode("utf-8")


def check_date(checkin_date, offer_dict):
  valid_offers = []

  #get date from user input
  checkin_date = datetime.strptime(checkin_date, '%Y-%m-%d')

  #get date from offer
  for offer in offer_dict.get('offers', []):
    valid_date = datetime.strptime(offer.get('valid_to', ''), '%Y-%m-%d')

    # Check if the offer is valid
    if valid_date >= checkin_date + timedelta(days=5):
      valid_offers.append(offer)
  offer_dict['offers'] = valid_offers
  return offer_dict

def check_cat(valid_categories: list, offer_dict):
  valid_offers= []

  for offer in offer_dict.get('offers', []):
    #check if the category is valid
    if offer['category'] in valid_categories: 
      valid_offers.append(offer)
    offer_dict['offers'] = valid_offers
  return offer_dict

def check_shortest_dis(offer_dict):
  for offer in offer_dict['offers']:
    #get min distance from each offer
    min_distance_offer = min(offer['merchants'], key=lambda x: x['distance'])
    offer['merchants'] = min_distance_offer
  return offer_dict

def check_shortest_dis_for_cat(offer_dict):
  #group same category
  group_cat = {}
  for offer in offer_dict.get('offers', []):
    if offer['category'] not in group_cat:
      group_cat[offer['category']] = [offer]
    else:
      group_cat[offer['category']].append(offer)

  #take shortest distance from each category
  shortest_distance_offers = []
  for sub_offer in group_cat.values():
    min_distance_offer = min(sub_offer, key=lambda x: x['merchants']['distance'])
    shortest_distance_offers.append(min_distance_offer)

  offer_dict['offers'] = shortest_distance_offers
  return offer_dict


def two_closest_offer(offer_dict):
  #get the 2 smallest distance offer
  smallest_two = heapq.nsmallest(2, offer_dict['offers'], key=lambda x: x['merchants']['distance'])
  offer_dict['offers'] = smallest_two
  return offer_dict


def return_offer(environ,offer_dict):
    query_string = environ.get('QUERY_STRING', '')
    query_params = str(parse.parse_qsl(query_string)[0][1])
    
    if not query_params:
        # Handle the case where no query parameters are present
        return "No query parameters found"
   
    #if parameter are present
    offer_dict = check_date(query_params,offer_dict)
    offer_dict = check_cat([1,2,4],offer_dict)
    offer_dict = check_shortest_dis(offer_dict)
    offer_dict = check_shortest_dis_for_cat(offer_dict)
    offer_dict = two_closest_offer(offer_dict)

    #output json file
    path = '../output.json'
    with open(path, 'w') as json_file:
      json.dump(offer_dict, json_file, indent=2)
    json_response = json.dumps(offer_dict,indent=2)
    # return str(offer_dict) 
    return json_response.encode("utf-8")

        

   