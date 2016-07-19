from app import app
from app.database import db_session
from app.models import User

if __name__ == '__main__':

    user = User('mensur', 'mandzuka')
    db_session.add(user)
    db_session.commit()
