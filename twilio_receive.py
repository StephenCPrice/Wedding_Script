from twilio.twiml.messaging_response import (
    MessagingResponse,
)  # this could be outdated I was using a different version of twilio - just wanted to get you started on receiving
from flask import Flask, request

app = Flask(__name__)

@app.route("/sms", methods=["GET", "POST"])

def sms_reply():
    resp = MessagingResponse()
    number = request.form["From"]
    message_body = request.form["Body"]
    print(message_body, number)

    resp.message(input("Enter Message: "))


if __name__ == "__main__":
    app.run(debug=True)
