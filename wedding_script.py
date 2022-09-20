import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def read_in_sheets(sheet_num):

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)

    client = gspread.authorize(creds)
    sheet = client.open('Master Wedding Planner')
    sheet_instance1 = sheet.get_worksheet(sheet_num)
    data = sheet_instance1.get_all_records()
    df = pd.DataFrame(data)

    return df


if __name__ == "__main__":

    sheet = read_in_sheets(0)
    print(sheet.head())