from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ..config import DATABASE_URI

engine = create_engine(DATABASE_URI)

Session = scoped_session(sessionmaker(bind=engine, autocommit=False))
