from sqlalchemy.orm import Session

from . import models, schemas


def get_user_id(db: Session):
    return db.query(models.Users.user_id).all()

