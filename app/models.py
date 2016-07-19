from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    created_on = Column(DateTime)

    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname = lastname