from flask import Flask
from routes import routes
from dotenv import load_dotenv
from database import create_table
import os

load_dotenv("creds.env")
key = os.environ.get("key")

app = Flask(__name__, static_folder='static')


app.secret_key = key
create_table()
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()
