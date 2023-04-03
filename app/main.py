from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing import List
from app.schemas import TeamCreate, PlayerCreate, GameCreate, Team, Player, Game
from app.database import get_db
from app import crud

app = FastAPI()


@app.post("/teams/", response_model=Team)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)


@app.get("/teams/", response_model=List[Team])
def read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)


@app.post("/players/", response_model=Player)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db, player)


@app.get("/players/", response_model=List[Player])
def read_players(db: Session = Depends(get_db)):
    return crud.get_players(db)


@app.get("/players/{player_name}", response_model=Player)
def read_player_by_name(player_name: str, db: Session = Depends(get_db)):
    return crud.get_player_by_name(db, player_name)


@app.post("/games/", response_model=Game)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db, game)


@app.get("/games/", response_model=List[Game])
def read_games(db: Session = Depends(get_db)):
    return crud.get_games(db)
