from github import Github
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from datetime import timedelta
import csv
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
SPREADSHEET_ID1 = config_vals['ID3']
SPREADSHEET_ID2 = config_vals['ID4']
sheetId = 1344422986
formula4 = config_vals['formula4']
save_path_extract5 = config_vals['save_path_extract5']
s = config_vals['g']
gg = Github(s)

t = config_vals['datetime']
tt = t.strftime('%Y%m%d')
datetime = t
print(datetime)
a = t
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
o = datetime - timedelta(days=14)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID1,
    range="7DAVRDLR14D!A1:I382").execute()
print(request)

RUN = [['' + formula4 + ',"'+str(a)+' - SUM!A1:I382")']]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID1,
    range="7DAVRDLR14D!A1",
    valueInputOption="USER_ENTERED", body={"values": RUN}).execute()
time.sleep(5)
print(request)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID1,
    range="7DAVRDLR14D!J2:X382").execute()
print(request)

RUN = [
    [
     '' + formula4 + ',"'+str(o)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(n)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(m)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(l)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(k)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(j)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(i)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(h)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(g)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(f)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(e)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(d)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(c)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(b)+' - SUM!F2:F382")', 
     '' + formula4 + ',"'+str(a)+' - SUM!F2:F382")'
    ]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID1,
    range="7DAVRDLR14D!J2",
    valueInputOption="USER_ENTERED", body={"values": RUN}).execute()
time.sleep(10)
print(request)


RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheetId,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 24,
        },
        "destination": {
            'sheetId': sheetId,
            'startRowIndex': 0,
            'endRowIndex': 382,
            'startColumnIndex': 0,
            'endColumnIndex': 24,
        },
        "pasteType": "Paste_Values",

    }},

]}
request3 = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID1,
    body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheetId,
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
    spreadsheetId=SPREADSHEET_ID1,
    body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheetId,
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
    spreadsheetId=SPREADSHEET_ID1,
    body=RUN).execute()
print(request)

client = gspread.authorize(creds)
spreadsheet = client.open_by_key(SPREADSHEET_ID1)
worksheetName = "7DAVRDLR14D"
worksheet = spreadsheet.worksheet(worksheetName)
filename = save_path_extract5 + tt + "_7DAVRDLR14D" + ".csv"
with open(filename, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(worksheet.get_all_values())

repo = gg.get_user().get_repo("SARS-CoV-2_PL_V_2.0")

file_path = save_path_extract5 + str(tt) + "_7DAVRDLR14D" + ".csv"
with open(file_path, 'r') as file:
    content = file.read()
repo.create_file(
    file_path,
    "Save: DATA/IOTR/" + str(tt) + "_7DAVRDLR14D" + ".csv",
    content)