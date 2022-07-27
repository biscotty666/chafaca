from curses import echo
from email.policy import default
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, create_engine

from datetime import datetime
import os

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.relpath(__file__))
connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'chafaca.db')
engine = create_engine(connection_string, echo=True)

Session = sessionmaker()

class Player(Base):
  __tablename__ = 'player'
  Id = Column(Integer(), primary_key=True)
  PlayerId = Column(String())
  AllyCode = Column(Integer())
  Name = Column(String(), nullable=False, unique=True)
  Level = Column(Integer())
  GuildRefId = Column(String())
  GuildName = Column(String())
  GuildBannerColor = Column(String())
  GuildBannerLogo = Column(String())
  GuildTypeId = Column(String())
  GrandArenaLifeTime = Column(Integer())
  Updated = Column(Integer())
  TimeStamp = Column(DateTime(), default=datetime.now)

  def __repr__(self):
    return f"<Id = {self.Id}\
        PlayerId = {self.PlayerId}\
        Name: name={self.Name}\
        Allycode: allyCode={self.AllyCode}\
        Level: level={self.Level}\
        GuildRefId={self.GuildRefId}\
        GuildName={self.GuildName}\
        GuildBannerColor={self.GuildBannerColor}\
        GuildBannerLogo={self.GuildBannerLogo}\
        GuildTypeId={self.GuildTypeId}\
        GrandArenaLifeTime={self.GrandArenaLifeTime}\
        Updated={self.Updated}\
        TimeStamp={self.TimeStamp}\
        >"

class Toon(Base):
  __tablename__ = 'player_toons'
  Id = Column(Integer(), primary_key=True)
  ToonId=Column(String())
  PlayerId = Column(String())
  DefId = Column(String())
  NameKey = Column(String())
  Rarity = Column(Integer())
  Level = Column(Integer())
  Xp = Column(Integer())
  Gear = Column(Integer())
  CombatType = Column(Integer())
  Gp = Column(Integer())
  PrimaryUnitStat = Column(String())
  Relic = Column(Integer())
  TimeStamp = Column(DateTime(), default=datetime.now)

  def __repr__(self):
    return f"<Id = {self.Id}\
        PlayerId = {self.PlayerId}\
        DefId = {self.PlayerId}\
        NameKey = {self.NameKey}\
        Rarity = {self.Rarity}\
        Level = {self.Level}\
        Xp = {self.Xp}\
        Gear = {self.Gear}\
        CombatType = {self.CombatType}\
        Gp = {self.Gp}\
        PrimaryUnitStat = {self.PrimaryUnitStat}\
        Relic = {self.Relic}\
        TimeStamp={self.TimeStamp}\
        >"

class Mod(Base):
  __tablename__ = 'toons_mods'
  Id=Column(Integer(), primary_key=True)
  ToonId=Column(String())
  ModId=Column(String())
  Level=Column(Integer())
  Tier=Column(Integer())
  Slot=Column(Integer())
  Set=Column(Integer())
  Pips=Column(Integer())

class ModStat(Base):
  __tablename__ = 'mods_stats'
  Id=Column(Integer(), primary_key=True)
  ModId=Column(String())
  UnitStat=Column(Integer())
  Value=Column(Integer())
  Roll=Column(Integer())
  StatType=Column(String())
  
