from app.database import Base, engine
from app.routers import games_router, players_router, teams_router
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(teams_router, prefix="/teams")
app.include_router(players_router, prefix="/players")
app.include_router(games_router, prefix="/games")

handler = Mangum(app)
