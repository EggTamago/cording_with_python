# now debug
import uvicorn

import secrets

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware

from urllib.error import HTTPError

app = FastAPI()

""" start CORS measures"""
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
""" end CORS measures"""

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "a")
    correct_password = secrets.compare_digest(credentials.password, "a")

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return username

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4040)