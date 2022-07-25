# For interaction with game api

from swgohhelp import SWGOHhelp, settings
import json
from pprint import pprint

with open('./config.json') as f:
  config = json.load(f)

# Make the connection
# creds = settings(config['CredName'], config['CredPass'], config['CredNum'], config['CredLet'])
creds = settings(config['swgohhelp']['credname'], config['swgohhelp']['credpass'], config['swgohhelp']['crednum'], config['swgohhelp']['credlet'])
client = SWGOHhelp(creds)

import requests

r = requests.get('https://swgoh-stat-calc.glitch.me/api/characters?flags=enums,gameStyle&useValues={char:{rarity:7,level:85,relic:5}}')

content = r.content
contentmod = content.decode('utf-8')
contentjson = json.loads(contentmod)

# pprint(str(contentjson))

with open('basestats.json', 'w') as f:
  json.dump(contentjson, f)

# import sqlite3

# conn = sqlite3.connect('chafaca.db')
# c = conn.cursor()

# c.execute("insert into guild values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
  
# )

# response = client.get_data('guild', config['allycodes'])
# with open('guild.json', 'w') as f:
#   json.dump(response, f)

# response = client.get_data('player', config['allycodes'])
# with open('player.json', 'w') as f:
#   json.dump(response, f)

