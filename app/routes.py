from flask_admin.contrib.sqla import ModelView
from app.models import User
from app import admin, db_session

# create view for User class
class UserView(ModelView):
    column_list = ('firstname', 'lastname')

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(User, session, **kwargs)

#bind UserView object to admin object
admin.add_view(UserView(db_session))
