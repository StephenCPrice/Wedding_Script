# To make it more reusable in the future it seems like using regex to find the headers and setting the head in line 29 to the row location(using gspread) might be good. That can be saved for later though.
# Come to think of it, you could use regex to find the headers, and then use that to also locate the exact header names to be used as the keys to iterate over. Let's build a v1 first though.
# Will need try and except blocks to return a log of whichever texts fail to send, although there shouldn't be any.

import gspread, re, os
from dotenv import (
    load_dotenv,
)  # loads enviornment variables from a given file, needed to share the .env file. Will be used with twilio
from oauth2client.service_account import ServiceAccountCredentials
from twilio.rest import Client
import pandas as pd
import time

load_dotenv("twilio_creds.env")


def get_sheet(sheet_name: str, credentials: str):
    # pass creds and return sheet object

    scope = ("https://www.googleapis.com/auth/drive",)
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)

    return sheet


def read_in_sheets(sheet_num: int) -> pd.DataFrame:
    # read in sheets to a pandas df

    sheet_instance1 = sheet.get_worksheet(sheet_num)
    df = pd.DataFrame(sheet_instance1.get_all_records(head=3))

    return df


def send_text(text: str, guest_number: str, client):
    # Placeholder function

    message = client.messages.create(body=text, from_="+14783775883", to=guest_number)
    print(message.sid)
    time.sleep(1)


if __name__ == "__main__":

    client = Client(os.environ["account_sid"], os.environ["auth_token"])

    sheet = get_sheet("Master Wedding Planner", "service_account.json")
    sheet_composite = read_in_sheets(1)

    sheet_composite["Phone Number"] = sheet_composite["Phone Number"].apply(
        lambda x: "+1" + x.replace("(", "").replace(")", "").replace("-", "")
    )

    for i, guest in enumerate(sheet_composite["First Name (s)"]):
        text = f"{guest}, we are pleased to invite you to our wedding! Please send back an RSVP."  # replace with actual invite
        send_text(text, sheet_composite["Phone Number"].loc[i], client)
