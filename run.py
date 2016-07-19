from app import app
from app.database import db_session
from app.models import User

if __name__ == '__main__':
    app.run(debug=True)
