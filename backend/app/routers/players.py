from typing import List

from app import crud
from app.database import get_db
from app.schemas import Player, PlayerCreate
from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

players_router = APIRouter()


@players_router.post("/", response_model=Player)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db, player)


@players_router.get("/", response_model=List[Player])
def read_players(db: Session = Depends(get_db)):
    return crud.get_players(db)


@players_router.get("/{player_name}", response_model=Player)
def read_player_by_name(player_name: str, db: Session = Depends(get_db)):
    return crud.get_player_by_name(db, player_name)
