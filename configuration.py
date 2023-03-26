from pydantic import BaseSettings


class Settings(BaseSettings):
    domain: str = "127.0.0.1"
    database_url: str = "sqlite:///./sql_app.db"

