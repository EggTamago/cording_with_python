from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models, schemas
# from .database import database, SessionLocal, engine
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# for slove CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@app.get("/")
def read_user(db: Session = Depends(get_db)):
    db_user = crud.get_user_id(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=4040)