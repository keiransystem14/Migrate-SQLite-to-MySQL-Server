from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize Database

app_db = SQLAlchemy()
DB_NAME = "account.db"



def create_application():
    app = Flask(__name__)  #Represents the name of the file.
    app.config['SECRET_KEY'] = 'DKJSDKFJSLDKFKJDKJF'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Incorrect SQLite link which is corrected to sqlite:///{DB_NAME}

    app_db.init_app(app)

    from .web_design import web_design
    from .login_auth import login_auth

    app.register_blueprint(web_design, url_prefix='/')
    app.register_blueprint(login_auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        app_db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'login_auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


"""

Removing this part of the code because it's not this is what's causing the errors. The reason why the errors exist is because Flask-SQLAlchemy 3 no longer supports the app argument in create_all
function. 

Flask-SQLAlchemy-3.0.5 is uninstalled and Flask-SQLAlchemy 2.5.0 is installed which did the fix but this will most likely not be a permenant fix depending on what we want to do with the
website.

"""
# def create_database(app):
#     if not path.exists('website/' + DB_NAME): #Syntax error by forgetting to include path.exists()
#         app_db.create_all(app=app)
#         print('Created Database!')