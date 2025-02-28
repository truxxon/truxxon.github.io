from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_wtf.csrf import CSRFProtect
import os


# Initialize database and CSRF protection
db = SQLAlchemy()
csrf = CSRFProtect()
DB_NAME = 'portfolio.db'

def create_app():

    app = Flask(__name__, instance_relative_config=True)  # ✅ Tells Flask to use the instance folder
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, DB_NAME)}"  # ✅ Correctly points to instance folder
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ✅ Prevents warnings
    db.init_app(app)
    csrf.init_app(app)  # Properly initialize CSRF protection

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    create_database(app)

    return app

def create_database(app):
    with app.app_context():  # ✅ Correct way to create tables
        db.create_all()
        print('[[[[[portfolio.db Created Successfully!]]]]]')




