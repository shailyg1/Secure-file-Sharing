from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from app.routes.ops_user import ops_user_bp
    from app.routes.client_user import client_user_bp

    app.register_blueprint(ops_user_bp, url_prefix="/ops")
    app.register_blueprint(client_user_bp, url_prefix="/client")

    return app
