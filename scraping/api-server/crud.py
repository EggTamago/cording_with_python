import random
from sqlalchemy.orm import Session

from . import models, schemas

def get_user_id(db: Session):

    # get data from db
    all_data = db.query(models.Actors.actor_name).all()

    # genarate random number between 0 to len(data)
    random_num = random.randint(0, len(all_data))

    # select the data to app and return
    return db.query(models.Actors.actor_name).filter(models.Actors.user_id == random_num).first()

