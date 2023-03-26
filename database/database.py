from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configuration import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = settings.database_url
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

if settings.env == "local":
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={}
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
