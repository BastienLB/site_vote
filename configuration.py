from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    env: str = "local"
    domain: str = "127.0.0.1:8000"
    database_url: str = "sqlite:///./sql_app.db"

