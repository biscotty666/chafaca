from classdef import Player, Session, Base, engine
import json
from datetime import datetime

Base.metadata.create_all(engine)

with open('player.json') as f:
  config = json.load(f)

config = config[0]
local_session = Session(bind=engine)

new_player = Player(PlayerId = config['id'],\
    Name = config['name'],\
    AllyCode = config['allyCode'],\
    Level = config['level'],\
    GuildRefId = config['guildRefId'],\
    GuildName = config['guildName'],\
    GuildBannerColor = config['guildBannerColor'],\
    GuildBannerLogo = config['guildBannerLogo'],\
    GuildTypeId = config['guildTypeId'],\
    GrandArenaLifeTime = config['grandArenaLifeTime'],\
    Updated = config['updated']
)

local_session.add(new_player)

local_session.commit()