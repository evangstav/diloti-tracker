from sqlalchemy.orm import Session
from app.schemas import TeamCreate, PlayerCreate, GameCreate
from app.models import Team as DBTeam, Player as DBPlayer, Game as DBGame
from fastapi import HTTPException


def create_team(db: Session, team: TeamCreate):
    if team.player1_name == team.player2_name:
        raise HTTPException(status_code=400, detail="Player names must be unique")

    existing_team = db.query(DBTeam).filter(DBTeam.name == team.name).first()
    if existing_team:
        db.close()
        raise HTTPException(status_code=400, detail="Team name already in use")

    db_team = DBTeam(name=team.name)
    player1 = get_or_create_player(db, team.player1_name)
    player2 = get_or_create_player(db, team.player2_name)

    db_team.players.extend([player1, player2])
    db.add(db_team)
    db.commit()
    db.refresh(db_team)

    return db_team


def get_teams(db: Session):
    return db.query(DBTeam).all()


def create_player(db: Session, player: PlayerCreate):
    db_player = DBPlayer(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_players(db: Session):
    return db.query(DBPlayer).all()


def get_player_by_name(db: Session, player_name: str):
    db_player = db.query(DBPlayer).filter(DBPlayer.name == player_name).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


def get_or_create_player(db: Session, player_name: str):
    player = db.query(DBPlayer).filter(DBPlayer.name == player_name).first()
    if not player:
        player = DBPlayer(name=player_name)
        db.add(player)
        db.flush()
    return player


def get_team_by_name(db: Session, team_name: str):
    db_team = db.query(DBTeam).filter(DBTeam.name == team_name).first()
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team


def create_game(db: Session, game: GameCreate):
    team1_id = get_team_by_name(db, game.team1_name).id
    team2_id = get_team_by_name(db, game.team2_name).id
    db_game = DBGame(
        team1_id=team1_id,
        team2_id=team2_id,
        team1_score=game.team1_score,
        team2_score=game.team2_score,
        timestamp=game.timestamp,
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_games(db: Session):
    return db.query(DBGame).all()
