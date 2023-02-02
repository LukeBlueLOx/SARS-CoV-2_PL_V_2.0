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
SPREADSHEET_ID1 = config_vals['ID2']
SPREADSHEET_ID2 = config_vals['ID4']
formula2 = config_vals['formula2']
sheet_id1 = '0'
t = config_vals['datetime']
sheet_id2 = t.strftime('%Y%m%d')

a = t
datetime = t
print(datetime)
b = datetime - timedelta(days=1)
c = datetime - timedelta(days=2)
d = datetime - timedelta(days=3)
e = datetime - timedelta(days=4)
f = datetime - timedelta(days=5)
g = datetime - timedelta(days=6)
h = datetime - timedelta(days=7)
i = datetime - timedelta(days=8)
j = datetime - timedelta(days=9)
k = datetime - timedelta(days=10)
l = datetime - timedelta(days=11)
m = datetime - timedelta(days=12)
n = datetime - timedelta(days=13)

RUN = [[str(t)]]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID1,
    range="COMPUTABLE!A2",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID1,
    range="COMPUTABLE!E3:E382").execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID1,
    range="COMPUTABLE!F3:F382").execute()
print(request)

RUN = [
    ["=({'"+str(n)+"'!I2}+{'"+str(m)+"'!I2}+{'"+str(l)+"'!I2}+{'"+str(k)+"'!I2}"
     "+{'"+str(j)+"'!I2}+{'"+str(i)+"'!I2}+{'"+str(h)+"'!I2}+{'"+str(g)+"'!I2}"
     "+{'"+str(f)+"'!I2}+{'"+str(e)+"'!I2}+{'"+str(d)+"'!I2}+{'"+str(c)+"'!I2}"
     "+{'"+str(b)+"'!I2}+{'"+str(a)+"'!I2})/I2"]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID1,
    range="COMPUTABLE!E2",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

RUN = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 1,
            'endRowIndex': 382,
            'startColumnIndex': 4,
            'endColumnIndex': 5
        }

    }}

]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID1,
    body=RUN).execute()
print(request)

RUN = [
    ["=({'"+str(g)+"'!H2}+{'"+str(f)+"'!H2}+{'"+str(e)+"'!H2}+{'"+str(d)+"'!H2}"
     "+{'"+str(c)+"'!H2}+{'"+str(b)+"'!H2}+{'"+str(a)+"'!H2})/7"]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID1,
    range="COMPUTABLE!F2",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

RUN = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 1,
            'endRowIndex': 382,
            'startColumnIndex': 5,
            'endColumnIndex': 6
        }
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID1,
    body=RUN).execute()
print(request)
time.sleep(7)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 1,
            'endRowIndex': 382,
            'startColumnIndex': 4,
            'endColumnIndex': 6
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 1,
            'endRowIndex': 382,
            'startColumnIndex': 4,
            'endColumnIndex': 6
        },
        "pasteType": "Paste_Values"

    }}

]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID1,
    body=RUN).execute()
print(request)

RUN = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": sheet_id2,
            "title": str(t) + " - SUM",
            "gridProperties": {
                "columnCount": 9,
                "rowCount": 382
            }
        },
    }},
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID2,
    body=RUN).execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID2,
    range=""+str(t)+" - SUM!A1:I382").execute()
print(request)

RUN = [[str(formula2)]]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID2,
    range=""+str(t)+" - SUM",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)
time.sleep(7)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 9
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 9
        },
        "pasteType": "Paste_Values"

    }}

]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID2,
    body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheet_id2,
            "startRowIndex": 1,
            "endRowIndex": 382,
            "startColumnIndex": 0,
            "endColumnIndex": 1
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID2,
    body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheet_id2,
            "startRowIndex": 1,
            "endRowIndex": 382,
            "startColumnIndex": 7,
            "endColumnIndex": 8
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID2,
    body=RUN).execute()
print(request)
