import requests
import pprint
import json
import os
#import pandas as pd
#import sqlalchemy as db
#from sqlalchemy import create_engine 
import ticketpy




#message: enter information at the prompt. All prompts must be answered. 

keyword_preference = input("Enter keyword:")
state_preference = input("Enter US state code:")
date_preference = input("Enter start date in the format 'yyyy-mm-dd' ")



#apikey = "HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g"
tm_client = ticketpy.ApiClient("HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g") 

pages = tm_client.events.find(
    classification_name='Hip-Hop',
    state_code='GA',
    start_date_time='2022-07-19T20:00:00Z',
    end_date_time='2022-07-21T20:00:00Z'
)

for page in pages:
    print(page)
    print(pages)
    for event in page:
        print(event)



#url = "https://app.ticketmaster.com/discovery/v2/events.json?{apikey}"
#url = "https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey={HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g}"
#url= 'https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey={apikey}'

#response = requests.get(url)

#print(response)



#if keyword_preference == keyword:
#   print(event)

#if city_preference == city:
#   print(event)



