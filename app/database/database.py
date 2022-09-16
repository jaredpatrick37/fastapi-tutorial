import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


PG_HOST = os.environ.get("DATABASE_HOST")
PG_DATABASE = os.environ.get("DATABASE_NAME")
PG_USERNAME = os.environ.get("DATABASE_USERNAME")

if os.path.exists("/secrets/database-password"):
    PG_PASSWORD = open("/secrets/database-password").read().strip()
else:
    PG_PASSWORD = None

SQLALCHEMY_DATABASE_URL = f"postgresql://{PG_USERNAME}:" \
    f"{PG_PASSWORD}@{PG_HOST}/{PG_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
