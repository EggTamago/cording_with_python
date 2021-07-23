from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from sqlalchemy.orm import sessionmaker

from db import database, engine
from users.models import Test

app = FastAPI()

# for slove CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# curl http://localhost:4040/
@app.get("/")
def get_root():
    
    SessionClass=sessionmaker(engine)
    session=SessionClass()

    users=session.query(Test.id).all()

    return users

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4040)