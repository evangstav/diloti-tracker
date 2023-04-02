from fastapi import Depends, FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import TeamCreate, PlayerCreate, GameCreate, Team, Player, Game
from app.models import Team as DBTeam, Player as DBPlayer, Game as DBGame, Base
from app.database import engine, get_db


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/teams/", response_model=Team)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    if team.player1_name == team.player2_name:
        raise HTTPException(status_code=400, detail="Player names must be unique")

    # Check if a team with the given name already exists
    existing_team = db.query(DBTeam).filter(DBTeam.name == team.name).first()
    if existing_team:
        db.close()
        raise HTTPException(status_code=400, detail="Team name already in use")

    db_team = DBTeam(name=team.name)

    # Check if players exist, create them if not
    player1 = db.query(DBPlayer).filter(DBPlayer.name == team.player1_name).first()
    if not player1:
        player1 = DBPlayer(name=team.player1_name)
        db.add(player1)
        db.flush()

    player2 = db.query(DBPlayer).filter(DBPlayer.name == team.player2_name).first()
    if not player2:
        player2 = DBPlayer(name=team.player2_name)
        db.add(player2)
        db.flush()

    db_team.players.extend([player1, player2])
    db.add(db_team)
    db.commit()
    db.refresh(db_team)

    return db_team


@app.get("/teams/", response_model=List[Team])
def read_teams(db: Session = Depends(get_db)):
    teams = db.query(DBTeam).all()
    return teams


@app.post("/players/", response_model=Player)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = DBPlayer(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


@app.get("/players/", response_model=List[Player])
def read_players(db: Session = Depends(get_db)):
    players = db.query(DBPlayer).all()
    return players


@app.get("/players/{player_name}", response_model=Player)
def read_player_by_name(player_name: str, db: Session = Depends(get_db)):
    # Query the database for a player with the given name
    db_player = db.query(DBPlayer).filter(DBPlayer.name == player_name).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


@app.post("/games/", response_model=Game)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    db_game = DBGame(
        team1_name=game.team1_name,
        team2_name=game.team2_name,
        team1_score=game.team1_score,
        team2_score=game.team2_score,
        date=game.date,
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


@app.get("/games/", response_model=List[Game])
def read_games(db: Session = Depends(get_db)):
    games = db.query(DBGame).all()
    return games
