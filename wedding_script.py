import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def get_sheet(sheet_name: str, creds: str):
    # pass creds and return sheet object

    scope = (
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    )
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)

    return sheet


def read_in_sheets(sheet_num: int) -> pd.DataFrame:
    # read in sheets to a pandas df

    sheet_instance1 = sheet.get_worksheet(sheet_num)
    df = pd.DataFrame(sheet_instance1.get_all_records())

    return df


if __name__ == "__main__":

    sheet = get_sheet("Master Wedding Planner", "service_account.json")
    df = read_in_sheets(0)
    print(df.head())
