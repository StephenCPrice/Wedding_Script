#To make it more reusable in the future it seems like using regex to find the headers and setting the head in line 25 to the row location(using gspread) might be good. That can be saved for later though.
#Come to think of it, you could use regex to find the headers, and then use that to also locate the exact header names to be used as the keys to iterate over. Let's build a v1 first though.
import gspread, twilio
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def get_sheet(sheet_name: str, credentials: str):
    # pass creds and return sheet object

    scope = (
        "https://spreadsheets.google.com/feeds", # I'm not sure if this is a valid scope, it is not listed https://developers.google.com/identity/protocols/oauth2/scopes.  
        "https://www.googleapis.com/auth/drive",
    )
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)

    return sheet


def read_in_sheets(sheet_num: int) -> pd.DataFrame:
    # read in sheets to a pandas df

    sheet_instance1 = sheet.get_worksheet(sheet_num)
    df = pd.DataFrame(sheet_instance1.get_all_records(head = 3)) 

    return df


if __name__ == "__main__":

    sheet = get_sheet("Master Wedding Planner", "service_account.json")
    df = read_in_sheets(0)
    print(df.head())

sheet_composite = read_in_sheets(1)                                  #  Grabs the data one time so as not to exceed google API's query limit.
for i in range(len(list(sheet_composite['First Name (s)']))):
    print((list(sheet_composite['First Name (s)'])[i]))
