from classdef import Toon, Mod, Session, Base, engine
import json
from datetime import datetime

from pprint import pprint

Base.metadata.create_all(engine)

with open('player.json') as f:
  config = json.load(f)

roster = config[0]['roster']

local_session = Session(bind=engine)

for toon in roster:
  mods = toon['mods']
  for mod in mods:
    new_mod = Mod(ToonId = toon['id'],\
      ModId = mod['id'],\
      Level = mod['level'],\
      Tier = mod['tier'],\
      Slot = mod['slot'],\
      Set = mod['set'],\
      Pips = mod['pips'],\
    )
    local_session.add(new_mod)

    local_session.commit()