from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
import os
from itsdangerous import URLSafeTimedSerializer
import configs
from dotenv import load_dotenv

load_dotenv("creds.env")
conn_credentials = os.environ.get("myql_creds")
app_key = os.environ.get("app_key")
serializer_key = os.environ.get("serializer_key")
db = SQLAlchemy()
mail = Mail()
serializer = URLSafeTimedSerializer(serializer_key)

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object(configs.Config)
    db.init_app(app)
    mail.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    with app.app_context():
        from routes import routes  # Import routes
        app.register_blueprint(routes)
        db.create_all()  # Create database tables for our data models
        app.secret_key = app_key
        return app
