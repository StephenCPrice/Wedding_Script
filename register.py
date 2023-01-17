import os
import psycopg2.extras
import psycopg2
import uuid
import bcrypt

from password_validation import PasswordPolicy
from dotenv import load_dotenv
from email_validator import validate_email, EmailNotValidError, EmailUndeliverableError

psycopg2.extras.register_uuid()
load_dotenv("creds.env")
conn_credentials = os.environ.get("psql_creds")


def register_user(email, password):

    password_validated = password_validation(password)
    email_validated = email_validation(email)
    email_is_unique = email_unique(email)
    #print(email_is_unique, email_validated, password_validated)

    if password_validated and email_validated and email_is_unique == True:
        salt = bcrypt.gensalt()
        user_id = uuid.uuid4()

        conn = psycopg2.connect(conn_credentials)
        cur = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        cur.execute("INSERT INTO users (email, password, salt, user_id) VALUES (%s, %s, %s, %s)",
                    (email, hashed_password, salt, user_id))
        conn.commit()
        cur.close()
        conn.close()
        return True

    elif password_validated is False:
        return 'Password not valid'
    elif email_validated is False:
        return 'Email not valid'
    elif email_is_unique is False:
        return 'Email not unique'


def password_validation(password):
    policy = PasswordPolicy(lowercase=1, uppercase=1, numbers=1, min_length=8)
    
    if policy.validate(password):
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


def email_unique(email):
    conn = psycopg2.connect(conn_credentials)
    cur = conn.cursor()
    cur.execute("SELECT email FROM users WHERE email = %s", (email,))
    query = cur.fetchall()
    cur.close()
    conn.close()

    # if list is empty return True
    if bool(query) is False:
        return True
    else:
        return False
