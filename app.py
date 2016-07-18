from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

# Wrap application
# name parameter is show on the default navebar
# for the view bootstrap 2 or 3 can be selected
admin = Admin(app, name='Flask admin example', template_mode='bootstrap3')

@app.route('/')
def hello():
    return 'Home page'

if __name__ == '__main__':
    app.run()
