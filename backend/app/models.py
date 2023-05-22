from datetime import datetime

from app.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# Association table for the many-to-many relationship between players and teams
player_team = Table(
    "player_team",
    Base.metadata,
    Column("player_id", Integer, ForeignKey("player.id"), primary_key=True),
    Column("team_id", Integer, ForeignKey("team.id"), primary_key=True),
)


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    nickname = Column(String, nullable=True)

    # Many-to-many relationship with teams
    teams = relationship("Team", secondary=player_team, back_populates="players")


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    # Many-to-many relationship with players
    players = relationship("Player", secondary=player_team, back_populates="teams")


class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True, autoincrement=True)
    team1_id = Column(Integer, ForeignKey("team.id"))
    team2_id = Column(Integer, ForeignKey("team.id"))
    team1_score = Column(Integer, nullable=True)
    team2_score = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    home_team = relationship("Team", foreign_keys=[team1_id])
    away_team = relationship("Team", foreign_keys=[team2_id])


class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer, ForeignKey("game.id"))
    round = Column(Integer, nullable=False)
    team_1_score = Column(Integer, nullable=False)
    team_2_score = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    game = relationship("Game", back_populates="score")


Game.score = relationship("Score", back_populates="game")
