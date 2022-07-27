from classdef import Toon, Skill, Session, Base, engine
import json

Base.metadata.create_all(engine)

with open('player.json') as f:
  config = json.load(f)

roster = config[0]['roster']

local_session = Session(bind=engine)

for toon in roster:
  skills = toon['skills']
  for skill in skills:
    new_skill = Skill(PlayerId = toon['id'],\
      SkillId = skill['id'],\
      Tier = skill['tier'],\
      NameKey = skill['nameKey'],\
      IsZeta = skill['isZeta'],\
      Tiers = skill['tiers']
    )

    local_session.add(new_skill)

    local_session.commit()