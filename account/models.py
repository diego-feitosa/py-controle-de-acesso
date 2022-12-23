from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from core.database import DBBaseModel


class AccountModel(DBBaseModel):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(256), index=True, nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    name = Column(String(256), nullable=True)
    activate = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)
