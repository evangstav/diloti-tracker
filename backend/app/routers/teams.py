from typing import List

from app import crud
from app.database import get_db
from app.schemas import Team, TeamCreate
from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

teams_router = APIRouter()


@teams_router.post("/", response_model=Team)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)


@teams_router.get("/", response_model=List[Team])
def read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)
