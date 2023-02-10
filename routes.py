from flask import Flask, request, redirect, render_template, Blueprint, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from twilio.twiml.messaging_response import MessagingResponse
from register import register_user
from login import authenticate_user
#from confirm_mail import confirm_the_email
from user_model import User
from __init__ import db, serializer
from datetime import datetime
routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(password, email)

        return authenticate_user(email, password)
        #login_user()
    return render_template('index.html', title='login')


@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(password, email)

        registration_result = register_user(email, password)

        if registration_result is True:
            flash('Please click the link in your email to confirm your account')
            return redirect(url_for('routes.login'))

        else:
            flash(f'{registration_result}')

    return render_template('register.html', title='register')

@routes.route('/confirm_email/<token>', methods=['GET', 'POST'])
def confirm_email(token):
    if request.method == 'GET':
        try:
            # Verify the token and get the email
            email = serializer.loads(token, salt='confirm-email') # max_age=3600
        except:
            flash('Invalid or expired token')
            return render_template('index.html', title='login')
        user = User.query.filter_by(email=email).first()
        if user:
            user.confirmed = True
            user.confirmed_on = datetime.utcnow()
            db.session.commit()
            flash('Email confirmed')
            return render_template('index.html', title='login')
        else:
            flash('User not found')

    return render_template('index.html', title='login')

@routes.route('/home')
@login_required
def home():
    logout_user()
    return render_template('home.html', title='home')

@routes.route("/sms", methods=['POST'])
def sms():
    # Get the incoming message
    message_body = request.form["Body"]
    print(message_body)
    # Create a Twilio response object
    resp = MessagingResponse()

    # Add a message to the response
    resp.message(
        "Please contact Stephen or Nicole for questions. Stephen can be reached at 832-341-9281, and Nicole at 713-417-3996")

    return str(resp)
