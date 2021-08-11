from pydantic import (BaseModel, Field)
from typing import Optional
from enum import Enum

class Team(str, Enum):
    away = 'away'
    home = 'home'

class Goal(BaseModel):
    player: Optional[str] = None
    team: Team

class Score(BaseModel):
    away: int=Field(ge=0, default=0)
    home: int=Field(ge=0, default=0)
    
class InfoTeam(BaseModel):
    team: Team
    name: Optional[str]
    country: Optional[str]
    league: Optional[str]
    stadium: Optional[str]