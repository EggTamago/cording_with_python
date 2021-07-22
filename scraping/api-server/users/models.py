from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, String

from db import metadata, engine

users = Table(
    __tablename__="test",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("num", Integer),
    Column("data", String)
)

metadata.create_all(bind=engine)