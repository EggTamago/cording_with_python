from sqlalchemy.orm import Session

from . import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).all()

def register_user(db: Session, name: str, passwword: str):
    # get User infomation

    # set register time stamp

    # add data to postgres
    return db.query(models.User).all()