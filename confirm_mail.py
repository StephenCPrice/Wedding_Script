'''from flask_mail import Message, Mail
from flask import Flask, request, redirect, render_template, Blueprint, flash, abort, url_for
from twilio.twiml.messaging_response import MessagingResponse
from flask_login import current_user
from bcrypt import gensalt, hashpw
import uuid
from datetime import datetime
from user_model import User
from __init__ import db, mail'''


'''def confirm_the_email(email):
    user = User.query.filter_by(email=email).first()
    if user and not user.confirmed:
        # Generate a confirmation token
        token = serializer.dumps(email, salt='email-confirmation')
        # Send the confirmation email with the token in the link
        msg = Message('Confirm Your Email', recipients=[email])
        msg.body = f'Please click the link to confirm your email: {url_for("routes.confirm_email", token=token, _external=True)}'
        mail.send(msg)
        flash('Confirmation email sent')
    return redirect(url_for('routes.login'))'''

'''def authenticate_email(email, code):
        query = db.session.query(User).filter_by(email=email).first()
        msg = Message(f'Confirm your email address {code}',
                      sender="from@example.com",
                      recipients=[f'{email}'])
        mail.send(msg)
        return code'''