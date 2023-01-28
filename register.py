import os
import psycopg2.extras
import psycopg2
import uuid
import sys

from flask_mail import Message, email_dispatched
from flask import redirect, url_for, flash, render_template
from datetime import datetime
from password_validation import PasswordPolicy
from dotenv import load_dotenv
from email_validator import validate_email, EmailNotValidError, EmailUndeliverableError
from user_model import User
from __init__ import db, serializer, mail
from bcrypt import gensalt, hashpw
from flask import current_app as app

psycopg2.extras.register_uuid()
load_dotenv("creds.env")
conn_credentials = os.environ.get("psql_credss")

def register_user(email, password):

    password_validated = password_validation(password)
    email_validated = email_validation(email)
    email_is_unique = email_unique(email)
    # print(email_is_unique, email_validated, password_validated)

    if password_validated and email_is_unique and email_validated == True:
        salt = gensalt()
        user_id = uuid.uuid4()
        hashed_password = hashpw(password.encode('utf-8'), salt)
        user = User(email=email, password=hashed_password,
                    salt=salt, user_id=user_id, created_on=datetime.utcnow(), authenticated=False, confirmed=False, confirmed_on=None, token=None)
        db.session.add(user)
        db.session.commit()
        print(user)
        confirm_the_email(user)
        return True
    elif password_validated is False:
        return 'Password not valid, please try again.'
    elif email_validated is False:
        return 'Email not valid, please try again.'
    elif email_is_unique is False:
        return 'Email not unique, please try again.'


def password_validation(password):
    policy = PasswordPolicy(lowercase=1, uppercase=1, numbers=1, min_length=8)
    return policy.validate(password)

def email_unique(email):
    query = db.session.query(User).filter_by(email=email).first()
    if query is None:
        return True
    else:
        return False

def email_validation(email):
    try:
        if validate_email(email):
            return True
        else:
            return False
    except (EmailNotValidError, EmailUndeliverableError) as e:
        return e

def confirm_the_email(user):
    if user and not user.confirmed:
        print(user.email, sys.stderr)
        # Generate a confirmation token
        token = serializer.dumps(user.email, salt='confirm-email')

        user.token = token
        db.session.commit()

        print(token, sys.stderr)
        # Send the confirmation email with the token in the link
        msg = Message('Confirm Your Email', recipients=[user.email])
        msg.body = f'Please click the link to confirm your email: {url_for("routes.confirm_email", token=token, _external=True)}'
        mail.send(msg)
    return render_template('index.html', title='login')

def log_message(message, app):
    app.logger.debug(message.subject)
    return render_template('index.html', title='login')

email_dispatched.connect(log_message)