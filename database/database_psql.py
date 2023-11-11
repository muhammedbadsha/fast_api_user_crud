from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config
from sqlalchemy.ext.declarative import declarative_base
URL_PSQL_DATABASE = config('URL_PSQL_DATABASE')

engine_psql = create_engine(URL_PSQL_DATABASE)

SessionLocalPsql = sessionmaker(autocommit=False, autoflush=True,bind=engine_psql)

Base = declarative_base()



