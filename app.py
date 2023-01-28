from __init__ import create_app

app = create_app()

'''from user_model import User
from routes import routes

load_dotenv("creds.env")
key = os.environ.get("key")
conn_credentials = os.environ.get("psql_credss")

Base = declarative_base()
from user_model import db
db.init_app(app)
db.create_all()
app.register_blueprint(routes)
'''

if __name__ == "__main__":
    app.run()
