from flask import Flask, request, render_template, Blueprint
from twilio.twiml.messaging_response import MessagingResponse

routes = Blueprint('routes', __name__)

@routes.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(password, email)
    return render_template('index.html', title='yoooo')

@routes.route("/sms", methods=['POST'])
def sms():
    # Get the incoming message
    message_body = request.form["Body"]
    print(message_body)
    # Create a Twilio response object
    resp = MessagingResponse()

    # Add a message to the response
    resp.message("Please contact Stephen or Nicole for questions. Stephen can be reached at 832-341-9281, and Nicole at 713-417-3996")

    return str(resp)