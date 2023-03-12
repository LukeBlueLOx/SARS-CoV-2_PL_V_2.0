from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import timedelta
import yaml
import time

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

SERVICE_ACCOUNT_FILE = ''+str(CORE)+'sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
Source1 = config_vals['Source6']
t = config_vals['datetime']
spreadsheet_id1 = config_vals['ID3']
sheet_id1 = 1677800535
tt = t - timedelta(days=1)
a = tt.strftime("%Y%m%d")
print (tt)
print(a)
filepaths1 = '' + str(Source1) + '' + str(a) + '.csv'
print(filepaths1)

request = sheet.values().clear(
    spreadsheetId=spreadsheet_id1,
    range="BVD!A1:M383").execute()
print(request)

RUN = [['=IMPORTDATA("' + str(filepaths1) + '";",")']]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id1,
    range="BVD!A1",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)
time.sleep(7)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 383,
            'startColumnIndex': 0,
            'endColumnIndex': 13
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 383,
            'startColumnIndex': 0,
            'endColumnIndex': 13
        },
        "pasteType": "Paste_Values"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1,
    body=RUN).execute()
print(request)

RUN = [[str(tt)]]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id1,
    range="VLP!E2",
    valueInputOption="USER_ENTERED", body={"values": RUN}).execute()
print(request)
time.sleep(10)
