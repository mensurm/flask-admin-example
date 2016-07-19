from flask_admin.contrib.sqla import ModelView
from flask.ext.admin import expose, BaseView
from app.models import User
from app import admin, db_session
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin

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

# 3. Serving files
# Exposing folder for add/rename/delete operations on static files
class FileView(FileAdmin):
    pass


#bind UserView object to admin object
admin.add_view(UserView(db_session))

#register static view on admin object
admin.add_view(StaticView(name="Static view"))

#register FileView on admin object
path = op.join(op.dirname(op.dirname(__file__)), 'static')
admin.add_view(FileView(path, name="Files"))
