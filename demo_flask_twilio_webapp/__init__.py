import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv()

db = SQLAlchemy()
DATABASE = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    # When in dev, uses DATABASE name
    # When in prod, use remote database URI (e.g., PostgreSQL on Heroku)
    # DO NOT place DATABASE_URL in .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{DATABASE}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .models import User

    create_database(app)

    from . import auth
    app.register_blueprint(auth.bp)

    # from . import message
    # app.register_blueprint(message.bp)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not os.path.exists('demo_flask_twilio_webapp/' + DATABASE):
        db.create_all(app=app)
        print(f'<Created Database File:{DATABASE}>')