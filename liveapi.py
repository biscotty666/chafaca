# For interaction with game api

from turtle import st
from swgohhelp import SWGOHhelp, settings
import json
import pprint

with open('./config.json') as f:
  config = json.load(f)

# Make the connection
# creds = settings(config['CredName'], config['CredPass'], config['CredNum'], config['CredLet'])
creds = settings(config['swgohhelp']['credname'], config['swgohhelp']['credpass'], config['swgohhelp']['crednum'], config['swgohhelp']['credlet'])
client = SWGOHhelp(creds)

response = client.get_data('guild', config['allycodes'])
with open('guild.json', 'w') as f:
  json.dump(response, f)

response = client.get_data('player', config['allycodes'])
with open('player.json', 'w') as f:
  json.dump(response, f)

