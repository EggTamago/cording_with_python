#===================================================
# SQLAlchemy uses the term "model" to refer to these classes and 
# instances that interact with the database.
#===================================================

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from database import Base

class Users(Base):
    __tablename__="users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)
    created_at = Column(DateTime(timezone=False), unique=False, nullable=False)
    updated_at = Column(DateTime(timezone=False), unique=False)
    deleted_at = Column(DateTime(timezone=False), unique=False)