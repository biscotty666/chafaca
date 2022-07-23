import json

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

