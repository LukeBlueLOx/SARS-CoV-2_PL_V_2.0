from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import timedelta
import yaml

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
Source1 = config_vals['Source1']
Source2 = config_vals['Source2']
t = config_vals['datetime']
spreadsheet_id1 = config_vals['ID1']
spreadsheet_id2 = config_vals['ID2']
spreadsheet_id3 = config_vals['ID3']
spreadsheet_id4 = config_vals['ID4']

yesterdayn = t - timedelta(days=13)
a = yesterdayn.strftime('%Y%m%d')
print(a)
yesterdayn = t - timedelta(days=33)
b = yesterdayn.strftime('%Y%m%d')
print(b)
tt = t.strftime('%Y%m%d')
print(tt)
c = yesterdayn = t - timedelta(days=14)
c = yesterdayn.strftime('%Y%m%d')
print(c)

request = sheet.values().clear(
    spreadsheetId=spreadsheet_id1,
    range="IOTR!A1:C28").execute()
print(request)

RUN = {'requests': [
    {
        "deleteSheet": {
            "sheetId": str(b)
        }
    },
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id1,
    body=RUN).execute()
print(request)


request = sheet.values().clear(
    spreadsheetId=spreadsheet_id2,
    range="COMPUTABLE!A2").execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=spreadsheet_id2,
    range="COMPUTABLE!E2:F382").execute()
print(request)

RUN = {'requests': [
    {
        "deleteSheet": {
            "sheetId": str(a)
        }
    },
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id2,
    body=RUN).execute()
print(request)


request = sheet.values().clear(
    spreadsheetId=spreadsheet_id3,
    range="IOTR!A2:D29").execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=spreadsheet_id3,
    range="7DAVRDLR14D!A2:X382").execute()
print(request)

RUN = {'requests': [
    {
        "deleteSheet": {
            "sheetId": str(tt) + '1'
        }
    },
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id4,
    body=RUN).execute()
print(request)

RUN = {'requests': [
    {
        "deleteSheet": {
            "sheetId": str(c)
        }
    },
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id4,
    body=RUN).execute()
print(request)
