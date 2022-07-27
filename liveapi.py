# For interaction with game api

from swgohhelp import SWGOHhelp, settings
import json
from pprint import pprint

with open('./config.json') as f:
  config = json.load(f)

# Connect to swgohhelp

# Get swgohhelp guild data
def ggd():
  creds = settings(config['swgohhelp']['credname'], config['swgohhelp']['credpass'], config['swgohhelp']['crednum'], config['swgohhelp']['credlet'])
  client = SWGOHhelp(creds)

  response = client.get_data('guild', config['allycodes'])
  with open('guild.json', 'w') as f:
    json.dump(response, f)

# Get swgohhelp player data
def gpd():
  creds = settings(config['swgohhelp']['credname'], config['swgohhelp']['credpass'], config['swgohhelp']['crednum'], config['swgohhelp']['credlet'])
  client = SWGOHhelp(creds)

  response = client.get_data('player', config['allycodes'])
  with open('player.json', 'w') as f:
    json.dump(response, f)

# Get base stat data from swgoh.gg
def gbs():
  import requests

  n = 1
  # f = open('basestats.json', 'w')
  # f.close()
  f = open('test.json', 'w')
  f.close()

  url = 'https://swgoh-stat-calc.glitch.me/api/characters?flags=enums,gameStyle&useValues={char:{rarity:7,level:85,gear:12}}'

  r = requests.get(url)
  content = r.content
  content = content.decode('utf-8')
  content = json.loads(content)

  with open(f'basestats12.json', 'w') as f:
      json.dump(content, f)


  while n<10:
    url = 'https://swgoh-stat-calc.glitch.me/api/characters?flags=enums,gameStyle&useValues={char:{rarity:7,level:85,relic:'+str(n)+'}}'

    r = requests.get(url)
    print(r)
    content = r.content
    content = content.decode('utf-8')
    content = json.loads(content)

    with open(f'basestats{n}.json', 'w') as f:
      json.dump(content, f)

    n += 1
  
  



gbs()
# import requests
# r = requests.get('https://swgoh-stat-calc.glitch.me/api/characters?flags=enums,gameStyle&useValues={char:{rarity:7,level:85,relic:1}}')

# print(r)
  
# gbs()