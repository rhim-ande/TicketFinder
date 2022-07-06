import requests
import pprint
import json
import os
import ticketpy


apikey = "HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g"
#url = 'https://app.ticketmaster.com/discovery/v2/events'
#response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=4dsfsf94tyghf85jdhshwge334')
#print(response)

response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey=HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g")
print(response.json())



#message: enter information at the prompt. All prompts must be answered. 

#keyword_preference = input("Enter keyword:")
#state_preference = input("Enter US state code:")
#date_preference = input("Enter start date in the format 'yyyy-mm-dd' ")



tm_client = ticketpy.ApiClient(apikey) 

pages = tm_client.events.find(
    classification_name='Hip-Hop',
    state_code='NY',
    start_date_time='2022-07-19T20:00:00Z',
    end_date_time='2022-07-21T20:00:00Z'
)


#for page in pages:
    #for event in page:
       # print(event)



        




#url = "https://app.ticketmaster.com/discovery/v2/events.json?{apikey}"
#url = "https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey={HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g}"
#url= 'https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey={apikey}'

#response = requests.get(url)

#print(response)



#if keyword_preference == keyword:
#   print(event)

#if city_preference == city:
#   print(event)



