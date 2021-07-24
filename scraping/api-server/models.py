
#===================================================
# SQLAlchemy uses the term "model" to refer to these classes and 
# instances that interact with the database.
#===================================================

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Integer, String

from .database import Base

class Test(Base):
    __tablename__="test"

    id = Column(Integer, index=True, primary_key=True),
    num = Column(Integer, primary_key=True),
    data = Column(String, primary_key=True)