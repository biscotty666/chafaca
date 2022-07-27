import json
import requests

from pprint import pprint

import discord
from discord.ext import commands

from api_swgoh_help import *

with open('./config.json') as f:
  config = json.load(f)
  
gg_client = api_swgoh_help(settings(config['gg']['username'], config['gg']['userpass']))

# Build local list of obtainable characters
payload = {}
payload['collection'] = "unitsList"
payload['language'] = "eng_us"
payload['enums'] = True
payload['match'] = {"rarity": 7,
                    "obtainable": True,
                    "obtainableTime": 0
                    }
payload['project'] = {"baseId": 1,
                      "nameKey": 1,
                      "descKey": 1,
                      "forceAlignment": 1,
                      "categoryIdList": 1,
                      "combatType": 1
                      }
units = gg_client.fetchData(payload)

with open('units.json', 'w') as f:
  for unit in units:
    json.dump(unit, f, indent = 4)

toons = {}
for unit in units:
    toons[unit['baseId']] = unit

with open('toons.json', 'w') as f:
  json.dump(toons, f, indent=4)

players = gg_client.fetchPlayers(config['allycodes'])

with open('players.txt', 'w') as f:
  f.write(str(players))

# urlBase = 'https://api.swgoh.help'
# signin = '/auth/signin'
# curl --location --request POST 'https://api.swgoh.help/auth/signin' \
# --header 'Method: POST' \
# --header 'Content-Type: application/x-www-form-urlencoded' \
# --data-urlencode 'username=test' \
# --data-urlencode 'password=test' \
# --data-urlencode 'grant_type=password' \
# --data-urlencode 'client_id=abc' \
# --data-urlencode 'client_secret=123'

header = {'Content-Type: application/x-www-form-urlencoded'}
data = {}
data = 'username='+config['gg']['username']
data += "&password="+config['gg']['userpass']


pprint(data)
# r = requests.post()

# payload = "username="+settings.username     
# user += "&password="+settings.password
#      self.user += "&grant_type=password"
#         self.user += "&client_id="+settings.client_id
#         self.user += "&client_secret="+settings.client_secret
    	    	
#         self.token = str()
            
    # self.user = "username="+settings.username     
    #     self.user += "&password="+settings.password
    #     self.user += "&grant_type=password"
    #     self.user += "&client_id="+settings.client_id
    #     self.user += "&client_secret="+settings.client_secret
    	    	
    #     self.token = str()
    
def get_token(self):
        sign_url = self.urlBase+self.signin
        payload = self.user
        head = {"Content-type": "application/x-www-form-urlencoded",
                'Content-Length': str(len(payload))}
        r = requests.request('POST',sign_url, headers=head, data=payload, timeout = 10)
        if r.status_code != 200:
            error = 'Cannot login with these credentials'
            return  {"status_code" : r.status_code,
                     "message": error}
        _tok = loads(r.content.decode('utf-8'))['access_token']
        self.token = { 'Authorization':"Bearer "+_tok} 
        return(self.token)

