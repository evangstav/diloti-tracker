from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import GameCreate, Game

from typing import List

games_router = APIRouter()


@games_router.post("/", response_model=Game)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db, game)


@games_router.get("/", response_model=List[Game])
def read_games(db: Session = Depends(get_db)):
    return crud.get_games(db)
