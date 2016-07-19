from flask_admin.contrib.sqla import ModelView
from flask.ext.admin import expose, BaseView
from app.models import User
from app import admin, db_session
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin

# 1. View created for CRUD operations on users table
# Inherits ModelView class
class UserView(ModelView):

    # For each class it can be defined if view can be accessed.
    # By default each view is accessible unless the opposite is explicitly set.
    # If there is a need for custom logic for determining access rights
    # is_accessible method should be overridden as shown below
    def is_accessible(self):
        return True        # most common usage would be  'return user.is_authenticated()'

    # parent class ModelView sets these properties to True by default
    # setting them to true in UserView can be ommited
    # it is set here just for illustration purposes
    can_edit = True
    can_delete = True
    can_edit = True
    column_list = ('firstname', 'lastname')

    column_filters = ('firstname', 'lastname')
    column_searchable_list = ('firstname', 'lastname')

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
    can_mkdir = False
    can_delete = True
    can_upload = True

#bind UserView object to admin object
admin.add_view(UserView(db_session))

#register static view on admin object
admin.add_view(StaticView(name="Static view"))

#register FileView on admin object
path = op.join(op.dirname(op.dirname(__file__)), 'static')
admin.add_view(FileView(path, name="Files"))
