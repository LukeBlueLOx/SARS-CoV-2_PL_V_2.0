from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import timedelta
import yaml
import time

with open("/home/blox_land/PycharmProjects/SARS-CoV-2_PL_V2/config_create_sheets.yaml", "r") as cr:
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
SPREADSHEET_ID = config_vals['ID2']
sheet_id1 = '0'
sheet_id2 = '208518000'
t = config_vals['datetime']

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
    spreadsheetId=SPREADSHEET_ID,
    range="DVSVL!A3",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID,
    range="DVSVL!C4:C382").execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID,
    range="TC!A4:A382").execute()
print(request)

RUN = [
    ["=({'"+str(n)+"'!I3}+{'"+str(m)+"'!I3}+{'"+str(l)+"'!I3}+{'"+str(k)+"'!I3}"
     "+{'"+str(j)+"'!I3}+{'"+str(i)+"'!I3}+{'"+str(h)+"'!I3}+{'"+str(g)+"'!I3}"
     "+{'"+str(f)+"'!I3}+{'"+str(e)+"'!I3}+{'"+str(d)+"'!I3}+{'"+str(c)+"'!I3}"
     "+{'"+str(b)+"'!I3}+{'"+str(a)+"'!I3})/E3"]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range="DVSVL!C3",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

RUN = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id1,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 2,
            'endColumnIndex': 3,
        },

    }},

]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body=RUN).execute()
print(request)

RUN = [
    ["=({'"+str(g)+"'!H3}+{'"+str(f)+"'!H3}+{'"+str(e)+"'!H3}+{'"+str(d)+"'!H3}"
     "+{'"+str(c)+"'!H3}+{'"+str(b)+"'!H3}+{'"+str(a)+"'!H3})/7"]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range="TC!A3",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

RUN = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id2,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        },

    }},

]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body=RUN).execute()
print(request)

time.sleep(10)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 2,
            'endColumnIndex': 3,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 2,
            'endColumnIndex': 3,
        },
        "pasteType": "Paste_Values",

    }},

]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body=RUN).execute()
print(request)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id2,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        },
        "destination": {
            'sheetId': sheet_id2,
            'startRowIndex': 2,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 1,
        },
        "pasteType": "Paste_Values",

    }},

]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body=RUN).execute()
print(request)

RUN = [
    ["=({'" + str(g) + "'!H2}+{'" + str(f) + "'!H2}+{'" + str(e) + "'!H2}+"
     "{'" + str(d) + "'!H2}+{'" + str(c) + "'!H2}+{'" + str(b) + "'!H2}+"
     "{'" +str(a) + "'!H2})/7"]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range="AVRXYPL!A1",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)
