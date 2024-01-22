from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """ User class definition"""
    __tablename__ = 'users'
    """ Table name """

    id = Column(Integer, primary_key=True)
    """ Column id """
    email = Column(String(250), nullable=False)
    """ Column email with 250 characters max """
    hashed_password = Column(String(250), nullable=False)
    """ Column hashed_password """
    session_id = Column(String(250), nullable=True)
    """ Column session_id """
    reset_token = Column(String(250), nullable=True)
    """ Column reset_token """
