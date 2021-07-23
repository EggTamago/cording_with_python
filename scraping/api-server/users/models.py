from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, String

from db import metadata, engine

Base = declarative_base()

class Test(Base):
    __tablename__="test",
    metadata,
    id = Column("id", Integer, primary_key=True, index=True),
    num = Column("num", Integer),
    data = Column("data", String)

    def test(self):
        return f'id:{self.id}, num:{self.num}, data:{self.data}'


metadata.create_all(bind=engine)