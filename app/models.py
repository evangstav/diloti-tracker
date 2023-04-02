from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from app.database import Base

player_team_association = Table(
    "player_team",
    Base.metadata,
    Column("team_id", Integer, ForeignKey("teams.name")),
    Column("player_id", Integer, ForeignKey("players.name")),
)


class Team(Base):
    __tablename__ = "teams"

    # id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, primary_key=True)
    players = relationship(
        "Player", secondary=player_team_association, back_populates="teams"
    )


class Player(Base):
    __tablename__ = "players"

    # id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, primary_key=True)
    teams = relationship(
        "Team", secondary=player_team_association, back_populates="players"
    )


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    team1_name = Column(String, ForeignKey("teams.name"))
    team2_name = Column(String, ForeignKey("teams.name"))
    team1_score = Column(Integer)
    team2_score = Column(Integer)
    date = Column(Date)

    team1 = relationship("Team", foreign_keys=[team1_name])
    team2 = relationship("Team", foreign_keys=[team2_name])
