from flask import Flask, request, redirect, render_template, Blueprint, flash
from twilio.twiml.messaging_response import MessagingResponse
from register import register_user

routes = Blueprint('routes', __name__)


@routes.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(password, email)
    return render_template('index.html', title='login')


@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(password, email)
        registration_result = register_user(email, password)
        if  registration_result is True:
            flash('Account created successfully')
            return redirect('/login')
        else:
            flash(f'{registration_result}')
    return render_template('register.html', title='register')


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
