from sqlalchemy import String, LargeBinary, TIMESTAMP
from __init__ import db
from datetime import datetime
from flask import current_app as app

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(255), primary_key=True)
    email = db.Column(String(255))
    password = db.Column(LargeBinary)
    salt = db.Column(LargeBinary)
    created_on = db.Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    authenticated = db.Column(db.Boolean, default=True)
    confirmed = db.Column(db.Boolean, nullable=True, default=False)
    confirmed_on = db.Column(TIMESTAMP, nullable=True)
    token = db.Column(String(255), nullable=True)

    def __init__(self, user_id, email, password, salt, created_on, authenticated, confirmed, confirmed_on, token):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.salt = salt
        self.created_on = created_on
        self.authenticated = authenticated
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
        self.token = token

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)