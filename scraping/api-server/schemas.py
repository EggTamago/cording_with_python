from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    num: int
    data: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True