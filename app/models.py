from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))

    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname = lastname