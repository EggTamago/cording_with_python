from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    num: int
    data: str

class Users(UserBase):
    id: int

    class Config:
        orm_mode = True