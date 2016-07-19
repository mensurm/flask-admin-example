from flask_admin.contrib.sqla import ModelView
from flask.ext.admin import expose, BaseView
from app.models import User
from app import admin, db_session

# 1. View created for CRUD operations on users table
# Inherits ModelView class
class UserView(ModelView):
    column_list = ('firstname', 'lastname')

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(User, session, **kwargs)

# 2. Static view
# Inherits BaseView class
class StaticView(BaseView):

    @expose('/', methods=('GET', 'POST'))
    def static_view(self):
        return self.render('admin/static_template.html')


#bind UserView object to admin object
admin.add_view(UserView(db_session))

#register static view on admin object
admin.add_view(StaticView(name="Static view"))
