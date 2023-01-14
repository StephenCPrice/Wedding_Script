import gspread
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Twilio Creds
TWILIO_PHONE_NUMBER = "+14783775883"
TWILIO_ACCOUNT_SID = "AC483698bc04b95d9174dc0f746e746399"
TWILIO_AUTH_TOKEN = "dcce89dc17958a6842ed35a1033535e8"

# Use a service account to authenticate to the Google Spreadsheet
gc = gspread.oauth() 

# Open the Google Spreadsheet
spreadsheet = gc.open("Master Wedding Planner")

# Select the desired worksheet
worksheet = spreadsheet.worksheet("Guests")

# Initialize the Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Iterate through the rows of the worksheet, starting from row 4
for i in range(71, worksheet.row_count):
    phone_number = worksheet.cell(i, 5).value
    first_name = worksheet.cell(i, 1).value
    last_name = worksheet.cell(i, 2).value
    guest_name = f"{first_name} {last_name}"

    try:
        # Send the save the date message to the phone number
        message = twilio_client.messages.create(
            to=phone_number,
            from_=TWILIO_PHONE_NUMBER,
            media_url=['https://i.imgur.com/ul9Wti3.jpeg'],
            body=f"Save the date! You are invited to the wedding of Stephen and Nicole. https://i.imgur.com/ul9Wti3.jpeg If you have any questions, please contact Stephen or Nicole at (713)417-3996"
        )
        print(f"Sent message to {guest_name} at {phone_number}")

        # Update the Spreadsheet with a "T" to indicate that the message was sent successfully
        worksheet.update_cell(i, 7, "T")
    except TwilioRestException:
        print(f"Failed to send message to {guest_name} at {phone_number}")

        # Update the Spreadsheet with an "F" to indicate that the message failed to send
        worksheet.update_cell(i, 7, "F")

print("Finished sending save the dates!")
