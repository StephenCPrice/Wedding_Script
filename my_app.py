from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from routes import routes

load_dotenv("creds.env")
key = os.environ.get("key")
conn_credentials = os.environ.get("psql_credss")

#Base = declarative_base()

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = conn_credentials
db = SQLAlchemy(app)

app.register_blueprint(routes)
return app


if __name__ == "__main__":
    create_app.run()
