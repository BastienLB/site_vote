from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    env: str = os.getenv("DOMAIN") if os.getenv("DOMAIN") is not None else "local"
    domain: str = os.getenv("DOMAIN") if os.getenv("DOMAIN") is not None else "127.0.0.1:8000"
    database_url: str = os.getenv("DATABASE_URL") if os.getenv("DATABASE_URL") is not None else "sqlite:///./sql_app.db"

