from google.oauth2 import service_account
from googleapiclient.discovery import build
from github import Github
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

config_vals = ""
with open(MAIN + "config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
datetime = config_vals['datetime']
s = config_vals['g']
g = Github(s)

config_vals = ""
with open(CORE + 'sunday_update/config_for_update_avr7d_array_range_7d_py.yaml',
          "r") as cr:
   config_vals = yaml.full_load(cr)
formula1 = config_vals['formula1']
formula11 = config_vals['formula11']
formula2 = config_vals['formula2']
a = config_vals['a']
b = config_vals['b']
c = config_vals['c']
d = config_vals['d']

nextday1 = datetime + timedelta(days=1)
a1 = nextday1.strftime('%Y-%m-%d')
nextday2 = datetime + timedelta(days=2)
b1 = nextday2.strftime('%Y-%m-%d')
nextday3 = datetime + timedelta(days=3)
c1 = nextday3.strftime('%Y-%m-%d')
nextday4 = datetime + timedelta(days=4)
d1 = nextday4.strftime('%Y-%m-%d')
nextday5 = datetime + timedelta(days=5)
e1 = nextday5.strftime('%Y-%m-%d')
nextday6 = datetime + timedelta(days=6)
f1 = nextday6.strftime('%Y-%m-%d')
nextday7 = datetime + timedelta(days=7)
g1 = nextday7.strftime('%Y-%m-%d')

a2 = nextday1.strftime('%Y-%m-%d')
b2 = nextday2.strftime('%Y-%m-%d')
c2 = nextday3.strftime('%Y-%m-%d')
d2 = nextday4.strftime('%Y-%m-%d')
e2 = nextday5.strftime('%Y-%m-%d')
f2 = nextday6.strftime('%Y-%m-%d')
g2 = nextday7.strftime('%Y-%m-%d')

nextday22 = datetime + timedelta(days=22)
a3 = nextday22.strftime('%Y-%m-%d')
nextday23 = datetime + timedelta(days=23)
b3 = nextday23.strftime('%Y-%m-%d')
nextday24 = datetime + timedelta(days=24)
c3 = nextday24.strftime('%Y-%m-%d')
nextday25 = datetime + timedelta(days=25)
d3 = nextday25.strftime('%Y-%m-%d')
nextday26 = datetime + timedelta(days=26)
e3 = nextday26.strftime('%Y-%m-%d')
nextday27 = datetime + timedelta(days=27)
f3 = nextday27.strftime('%Y-%m-%d')
nextday28 = datetime + timedelta(days=28)
g3 = nextday28.strftime('%Y-%m-%d')
spreadsheet_id = '17rIcj6djv7NmIC3RV16VGVkv7tTJgUd8UGvk8ruMOmU'
sheet_id = '0'

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': a,
            'endRowIndex': b,
            'startColumnIndex': 7,
            'endColumnIndex': 20,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': b,
            'endRowIndex': c,
            'startColumnIndex': 7,
            'endColumnIndex': 20,
        },
        "pasteType": "Paste_FORMULA",
    }},
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id, body=RUN).execute()
print(request)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': a,
            'endRowIndex': b,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': a,
            'endRowIndex': b,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "pasteType": "Paste_VALUES",
    }},
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id, body=RUN).execute()
print(request)

RUN = [
    ['=IF(G:G="","",B'+str(b)+')', '=IF(G:G="","",C'+str(b)+')',
     '=IF(G:G="","",D'+str(b)+')', '=IF(G:G="","",E'+str(b)+')',
     '=IF(G:G="","",F'+str(b)+')', '=IF(G:G="","",G'+str(b)+')',
     ''+str(formula1)+',"'+str(a2)+'!E2")'],
    ['=IF(G:G="","",C'+str(b)+')', '=IF(G:G="","",D'+str(b)+')',
     '=IF(G:G="","",E'+str(b)+')', '=IF(G:G="","",F'+str(b)+')',
     '=IF(G:G="","",G'+str(b)+')',
     ''+str(formula11)+', "'+str(a2)+'!E2"))',
     ''+str(formula1)+', "'+str(b2)+'!E2")'],
    ['=IF(G:G="","",D'+str(b)+')', '=IF(G:G="","",E'+str(b)+')',
     '=IF(G:G="","",F'+str(b)+')', '=IF(G:G="","",G'+str(b)+')',
     ''+str(formula11)+', "'+str(a2)+'!E2"))',
     ''+str(formula11)+', "'+str(b2)+'!E2"))',
     ''+str(formula1)+', "'+str(c2)+'!E2")'],
    ['=IF(G:G="","",E'+str(b)+')', '=IF(G:G="","",F'+str(b)+')',
     '=IF(G:G="","",G'+str(b)+')',
     ''+str(formula11)+', "'+str(a2)+'!E2"))',
     ''+str(formula11)+', "'+str(b2)+'!E2"))',
     ''+str(formula11)+', "'+str(c2)+'!E2"))',
     ''+str(formula1)+', "'+str(d2)+'!E2")'],
    ['=IF(G:G="","",F'+str(b)+')', '=IF(G:G="","",G'+str(b)+')',
     ''+str(formula11)+', "'+str(a2)+'!E2"))',
     ''+str(formula11)+', "'+str(b2)+'!E2"))',
     ''+str(formula11)+', "'+str(c2)+'!E2"))',
     ''+str(formula11)+', "'+str(d2)+'!E2"))',
     ''+str(formula1)+', "'+str(e2)+'!E2")'],
    ['=IF(G:G="","",G'+str(b)+')',
     ''+str(formula11)+', "'+str(a2)+'!E2"))',
     ''+str(formula11)+', "'+str(b2)+'!E2"))',
     ''+str(formula11)+', "'+str(c2)+'!E2"))',
     ''+str(formula11)+', "'+str(d2)+'!E2"))',
     ''+str(formula11)+', "'+str(e2)+'!E2"))',
     ''+str(formula1)+', "'+str(f2)+'!E2")'],
    [''+str(formula11)+', "'+str(a2)+'!E2"))',
     ''+str(formula11)+', "'+str(b2)+'!E2"))',
     ''+str(formula11)+', "'+str(c2)+'!E2"))',
     ''+str(formula11)+', "'+str(d2)+'!E2"))',
     ''+str(formula11)+', "'+str(e2)+'!E2"))',
     ''+str(formula11)+', "'+str(f2)+'!E2"))',
     ''+str(formula1)+', "'+str(g2)+'!E2")']
]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range="7DAVR!A"+str(d)+"",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

RUN = [
    ['=IF(H:H="","",'+str(formula2)+', "'+str(a2)+'!M2"))',
     '=IF(H:H="","",'+str(formula2)+', "'+str(a2)+'!I2"))'],
    ['=IF(H:H="","",'+str(formula2)+', "'+str(b2)+'!M2"))',
     '=IF(H:H="","",'+str(formula2)+', "'+str(b2)+'!I2"))'],
    ['=IF(H:H="","",'+str(formula2)+', "'+str(c2)+'!M2"))',
     '=IF(H:H="","",'+str(formula2)+', "'+str(c2)+'!I2"))'],
    ['=IF(H:H="","",'+str(formula2)+', "'+str(d2)+'!M2"))',
     '=IF(H:H="","",'+str(formula2)+', "'+str(d2)+'!I2"))'],
    ['=IF(H:H="","",'+str(formula2)+', "'+str(e2)+'!M2"))',
     '=IF(H:H="","",'+str(formula2)+', "'+str(e2)+'!I2"))'],
    ['=IF(H:H="","",'+str(formula2)+', "'+str(f2)+'!M2"))',
     '=IF(H:H="","",'+str(formula2)+', "'+str(f2)+'!I2"))'],
    ['=IF(H:H="","",'+str(formula2)+', "'+str(g2)+'!M2"))',
     '=IF(H:H="","",'+str(formula2)+', "'+str(g2)+'!I2"))']
]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range="7DAVR!M"+str(d)+"",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=spreadsheet_id,
    range="7DAVR!I"+str(d)+":I"+str(c)+"").execute()
print(request)

RUN = [
    ['=IF(H:H="","","'+str(a1)+'")'],
    ['=IF(H:H="","","'+str(b1)+'")'],
    ['=IF(H:H="","","'+str(c1)+'")'],
    ['=IF(H:H="","","'+str(d1)+'")'],
    ['=IF(H:H="","","'+str(e1)+'")'],
    ['=IF(H:H="","","'+str(f1)+'")'],
    ['=IF(H:H="","","'+str(g1)+'")']
]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range="7DAVR!I"+str(d)+"",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=spreadsheet_id,
    range="7DAVR!O"+str(d)+":O"+str(c)+"").execute()
print(request)

RUN = [
    ['=IF(N:N="","","'+str(a3)+'")'],
    ['=IF(N:N="","","'+str(b3)+'")'],
    ['=IF(N:N="","","'+str(c3)+'")'],
    ['=IF(N:N="","","'+str(d3)+'")'],
    ['=IF(N:N="","","'+str(e3)+'")'],
    ['=IF(N:N="","","'+str(f3)+'")'],
    ['=IF(N:N="","","'+str(g3)+'")']
]
request = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range="7DAVR!O"+str(d)+"",
    valueInputOption="USER_ENTERED", body={"values": RUN}).execute()
print(request)

"""e = b - 1
RUN = {'requests': [
    {'autoFill': {
        'range': {
            'sheetId': sheet_id,
            'startRowIndex': e,
            'endRowIndex': c,
            'startColumnIndex': 16,
            'endColumnIndex': 20,
        },
    }},
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id, body=RUN).execute()
print(request)"""

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id,
            'startRowIndex': a,
            'endRowIndex': b,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "destination": {
            'sheetId': sheet_id,
            'startRowIndex': b,
            'endRowIndex': c,
            'startColumnIndex': 0,
            'endColumnIndex': 20,
        },
        "pasteType": "Paste_FORMAT",
    }},
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id, body=RUN).execute()
print(request)

config_vals['a'] = a + 7
with open(CORE + 'sunday_update/config_for_update_avr7d_array_range_7d_py'
                 '.yaml',
          "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['b'] = b + 7
with open(CORE + 'sunday_update/config_for_update_avr7d_array_range_7d_py'
                 '.yaml',
          "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)
   
config_vals['c'] = c + 7
with open(CORE + 'sunday_update/config_for_update_avr7d_array_range_7d_py'
                 '.yaml',
          "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)

config_vals['d'] = d + 7
with open(CORE + 'sunday_update/config_for_update_avr7d_array_range_7d_py'
                 '.yaml',
          "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)

repo = g.get_user().get_repo("scv2pl")
contents = repo.get_contents('/CORE/sunday_update/config_for_update_avr7d_arr'
                              'ay_range_7d_py.yaml')
with open(CORE + 'sunday_update/config_for_update_avr7d_array_range_7d_py'
                 '.yaml',
          'r') as file:
    content = file.read()
# update
repo.update_file(contents.path,
                 "Save: config_for_update_avr7d_array_range_7d_py.yaml",
                 content,
                 contents.sha)
print(content)

repo = g.get_user().get_repo("SARS-CoV-2_PL_V_2.0")
contents = repo.get_contents('/CORE/sunday_update/config_for_update_avr7d_arr'
                              'ay_range_7d_py.yaml')
with open(CORE + 'sunday_update/config_for_update_avr7d_array_range_7d_py'
                 '.yaml',
          'r') as file:
    content = file.read()
# update
repo.update_file(contents.path,
                 "Save: config_for_update_avr7d_array_range_7d_py.yaml",
                 content,
                 contents.sha)
print(content)