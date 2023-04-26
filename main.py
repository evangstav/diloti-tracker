from fastapi import FastAPI
from app.database import engine, Base
from app.routers import teams_router, players_router, games_router
from mangum import Mangum

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(teams_router, prefix="/teams")
app.include_router(players_router, prefix="/players")
app.include_router(games_router, prefix="/games")

handler = Mangum(app)
