from typing import List, Optional

from pydantic import BaseModel
from pydantic.types import OptionalDate


class TeamBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class TeamCreate(TeamBase):
    player1_name: str
    player2_name: str


class PlayerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    teams: Optional[List[TeamBase]] = []

    class Config:
        orm_mode = True


Player.update_forward_refs()


class Team(TeamBase):
    id: int
    players: Optional[List["Player"]] = []

    class Config:
        orm_mode = True


Team.update_forward_refs()


class GameBase(BaseModel):
    team1_id: str
    team2_id: str
    team1_score: int
    team2_score: int
    timestamp: OptionalDate


class GameCreate(BaseModel):
    team1_name: str
    team2_name: str
    team1_score: int
    team2_score: int
    timestamp: OptionalDate


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True
