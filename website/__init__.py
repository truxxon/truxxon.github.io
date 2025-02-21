from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_wtf.csrf import CSRFProtect
import os

# Initialize database and CSRF protection
db = SQLAlchemy()
csrf = CSRFProtect()
DB_NAME = 'my_database.db'

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'ASDFGHJKL'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    csrf.init_app(app)  # Properly initialize CSRF protection

    from .views import views
    # from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    print("Registered routes:")
    print(app.url_map)


    # app.register_blueprint(auth, url_prefix="/")  # ✅ Fixed Typo

    # from .models import Artwork, Commission

    create_database(app)

    return app

def create_database(app):
    with app.app_context():  # ✅ Correct way to create tables
        if not path.exists(DB_NAME):  # ✅ Fix: Don't assume "website/"
            db.create_all()
            print('BimBapBam Database Created!')




