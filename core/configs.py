import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    PORT: int = int(os.getenv('APP_PORT'))
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    ALGORITHM: str = os.getenv('ALGORITHM')
    TOKEN_EXPIRE_MINUTES: int = os.getenv('TOKEN_EXPIRE_MINUTES')

    class Config:
        case_sensitive: True


class Database(BaseSettings):
    _ENGINE = os.getenv('DB_ENGINE')
    _HOST = os.getenv('DB_HOST')
    _PORT = os.getenv('DB_PORT')
    _NAME = os.getenv('DB_NAME')
    _USER = os.getenv('DB_USERNAME')
    _PASS = os.getenv('DB_PASSWORD')

    DB_URL: str = f'{_ENGINE}://{_USER}:{_PASS}@{_HOST}:{_PORT}/{_NAME}'

    class Config:
        case_sensitive: True


settings: Settings = Settings()
database: Database = Database()
