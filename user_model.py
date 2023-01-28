
from sqlalchemy.dialects.postgresql import UUID
from __init__ import db
from datetime import datetime
from flask_login import UserMixin
from flask import current_app as app

class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String)
    password = db.Column(db.LargeBinary)
    salt = db.Column(db.LargeBinary)
    user_id = db.Column(UUID(as_uuid=True), primary_key=True)
    created_on = db.Column(db.TIMESTAMP, nullable=False,
                           default=datetime.utcnow)
    authenticated = db.Column(db.Boolean, default=True)
    confirmed = db.Column(db.Boolean, nullable=True, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    token = db.Column(db.String, nullable=True)

    def __init__(self, email, password, salt, user_id, created_on, authenticated, confirmed, confirmed_on, token):
        self.email = email
        self.password = password
        self.salt = salt
        self.user_id = user_id
        self.created_on = created_on
        self. authenticated = authenticated
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