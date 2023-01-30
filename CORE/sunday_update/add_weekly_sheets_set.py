from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import timedelta
import yaml

SERVICE_ACCOUNT_FILE = '/app/CORE/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

config_vals = ""
with open("/app/config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
n = config_vals['n']
datetime = config_vals['datetime']
spreadsheet_id1 = config_vals['ID1']
spreadsheet_id2 = config_vals['ID2']

while n < 7:
    config_vals = ""
    with open("/app/config_create_sheets.yaml", "r") \
            as cr:
        config_vals = yaml.full_load(cr)
        n = config_vals['n']

    day_n = datetime + timedelta(days=n)
    a = day_n.strftime('%Y%m%d')
    b = day_n.strftime('%Y-%m-%d')
    print(a)
    print(b)

    RUN1 = {'requests': [
        {'addSheet': {
            'properties': {
                "sheetId": a,
                "title": b,
            },
        }},
    ]}
    request1 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN1).execute()
    print(request1)

    RUN2 = {'requests': [
        {'addSheet': {
            'properties': {
                "sheetId": a,
                "title": b,
            },
        }},
    ]}
    request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id2, body=RUN2).execute()
    print(request2)

    config_vals['n'] = n + 1
    with open("/app/config_create_sheets.yaml",
              "w") as cw:
        yaml.dump(config_vals, cw, default_flow_style=True)

    continue

    break  # exit

# n=7
