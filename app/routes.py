from flask_admin.contrib.sqla import ModelView
from flask.ext.admin import expose, BaseView, AdminIndexView
from app.models import User
from app import admin, db_session
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin
from datetime import datetime
from flask import redirect
from app import app

# by default entry point for admin application is /admin
# adding this redirect shows the admin app as the home page
@app.route('/', methods=('GET', 'POST'))
def home_page():
    return redirect('/admin')

# Using a custom base class enables configuration on a application level
# If the application should be exposed only to authenticated users
# this would be the place to check user privileges
class ApplicationBaseView():
    def is_accessible(self):
        return True         # sample application has no authentication
                            # in case the opposite is correct this method could return the following:
                            # 'return user.is_authenticated()'

class ApplicationIndexView(ApplicationBaseView, AdminIndexView):
    @expose('/', methods=('GET'))
    def index_view(self):
        return self.render('admin/index.html')


# 1. View created for CRUD operations on users table
# Inherits ModelView class
class UserView(ApplicationBaseView, ModelView):

    # For each class it can be defined if view can be accessed.
    # By default each view is accessible unless the opposite is explicitly set.
    # If there is a need for custom logic for determining access rights
    # is_accessible method should be overridden as shown below
    def is_accessible(self):
        return True

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.created_on = datetime.now()

    # parent class ModelView sets these properties to True by default
    # setting them to true in UserView can be ommited
    # it is set here just for illustration purposes
    can_edit = True
    can_delete = True
    can_edit = True
    column_list = ('firstname', 'lastname')
    form_excluded_columns = ('created_on')

    column_filters = ('firstname', 'lastname')
    column_searchable_list = ('firstname', 'lastname')

    can_export = True
    can_view_details = True

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(User, session, **kwargs)

# 2. Static view
# Inherits BaseView class
class StaticView(ApplicationBaseView, BaseView):

    @expose('/', methods=('GET', 'POST'))
    def static_view(self):
        return self.render('admin/static_template.html')

    @expose('/time', methods=('GET', 'POST'))
    def show_time(self):
        return self.render('admin/time.html', time=datetime.now())

# 3. Serving files
# Exposing folder for add/rename/delete operations on static files
class FileView(ApplicationBaseView, FileAdmin):
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
