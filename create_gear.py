from classdef import Toon, Gear, Session, Base, engine
import json
from datetime import datetime

Base.metadata.create_all(engine)

with open('player.json') as f:
  config = json.load(f)

roster = config[0]['roster']

local_session = Session(bind=engine)

for toon in roster:
  gears = toon['equipped']
  for gear in gears:
    new_gear = Gear(PlayerId = toon['id'],\
      GearId = gear['equipmentId'],\
      Slot = gear['slot'],\
      NameKey = gear['nameKey']
    )
    local_session.add(new_gear)

    local_session.commit()