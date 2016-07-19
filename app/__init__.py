from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from database import db_session

app = Flask(__name__)
db = SQLAlchemy()

# Wrap application
# name parameter is show on the default navebar
# for the view bootstrap 2 or 3 can be selected
admin = Admin(app, name='Flask admin example', template_mode='bootstrap3')

@app.route('/')
def hello():
    return 'Home page'

# Close db session after application context shutdown
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
