from flask import Flask
from flask_admin import Admin
from database import db_session

app = Flask(__name__)
app.secret_key = u'awp33dac3.asd32axWd2e'

# Wrap application
# name parameter is show on the default navebar
# for the view bootstrap 2 or 3 can be selected
admin = Admin(app, name='Flask admin example', template_mode='bootstrap3')

# Close db session after application context shutdown
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from app import routes