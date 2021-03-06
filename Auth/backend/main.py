
import uvicorn

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import db_session, engine
import models

# ここでDB初期化(Baseを継承したclass tableを作成する)
models.Base.metadata.create_all(bind=engine)

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

class User(BaseModel):
    username: str
    password: str

# in production you can use Settings management
# from pydantic to get secret key from .env
class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {"cookies"}
    # Only allow JWT cookies to be sent over https
    authjwt_cookie_secure: bool = True
    # Enable csrf double submit protection. default is True
    authjwt_cookie_csrf_protect: bool = False
    # Change to 'lax' in production to make your website more secure from CSRF Attacks, default is None
    authjwt_cookie_samesite: str = 'none'

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()

# exception handler for authjwt
# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    print("error occured")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

# register user name and password
@app.post('/register')
def register(register: User, Authorize: AuthJWT = Depends()):
    # check input data from web app
    name = register.name
    password = register.password

    # 登録済のnameがあればreturn

    # なければpasswordをhash化して登録
    # passwordに登録日付の末尾３桁取得してhashしてhashした番号を登録

    # 無事登録出来たらreturn success

    


    # return success to register 
    return {"register success"}

# provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token to use authorization
# later in endpoint protected
@app.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):
    if user.username != "tani" or user.password != "test":
        raise HTTPException(status_code=401,detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.username)

    print("log in")

    # Set the JWT cookies in the response
    Authorize.set_access_cookies(access_token)
    return {"access_token":access_token}


@app.delete('/logout')
def logout(Authorize: AuthJWT = Depends()):
    """
    Because the JWT are stored in an httponly cookie now, we cannot
    log the user out by simply deleting the cookies in the frontend.
    We need the backend to send us a response to delete the cookies.
    """
    Authorize.jwt_required()

    print("log out")

    Authorize.unset_jwt_cookies()
    return {"msg":"Successfully logout"}

# protect endpoint with function jwt_required(), which requires
# a valid access token in the request headers to access.
@app.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    print("call user")

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4040)