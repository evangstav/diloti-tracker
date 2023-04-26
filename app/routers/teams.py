from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import Team, TeamCreate

from typing import List

teams_router = APIRouter()


@teams_router.post("/", response_model=Team)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)


@teams_router.get("/", response_model=List[Team])
def read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)
