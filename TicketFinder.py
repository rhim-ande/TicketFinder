import requests
import pprint
import json
import os
import pandas as pd
#import ticketpy

apikey = os.environ.get('tm_apikey')  # <~ source key in ~/.bashrc OR create .env file
params = dict(apikey=apikey)

url = ('https://app.ticketmaster.com/')
events = ('discovery/v2/events.json')
size = ('size=1')

response = requests.get(url + events + size, params=params)
#apikey = "HYTeCD8nCfFuOtQog8WunqWnAgA5eS1g"
#url = 'https://app.ticketmaster.com/discovery/v2/events'
#response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=4dsfsf94tyghf85jdhshwge334')
#print(response)


data = response.json()
#print(data[events])

#js = json.dump("event", "name")
#print(js)

js = json.loads(data)
df2 = json_normalized(js['events'])

df2 = pd.read_json(data, orient = 'index')

print(df2)











