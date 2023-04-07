from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from os import environ

env = environ.get("ENV", "dev")
HOSTNAME = environ.get("HOSTNAME")
USER = environ.get("USER")
PASSWORD = environ.get("PASSWORD")
DB_NAME = environ.get("DB_NAME")

if env == "prod":
    DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOSTNAME}/{DB_NAME}"
else:
    DATABASE_URL = "sqlite:///./game_scores.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
