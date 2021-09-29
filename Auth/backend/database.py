from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#============================
# 参考：https://fastapi.tiangolo.com/advanced/async-sql-databases/
#============================

DATABASE = 'postgresql'
USER =     'admin'
PASSWORD = 'password'
HOST =     '192.168.30.1'
PORT =     '5432'
DB_NAME =  'data_visualization'

# DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

# どのDBに接続か指定
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# DBとのセッション
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DBを作成して初期化
Base = declarative_base()
