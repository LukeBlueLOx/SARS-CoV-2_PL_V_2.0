from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import date, timedelta
import yaml

SERVICE_ACCOUNT_FILE = '/app/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

config_vals = ""
with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
n = config_vals['n']
spreadsheet_id1 = config_vals['ID1']
spreadsheet_id2 = config_vals['ID2']

date_components = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
print(date_components)
year, month, day = [int(item) for item in date_components]
date_input = date(year, month, day)
print(date_input)
config_vals['datetime'] = date_input
with open("config_create_sheets.yaml",
          "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)

while n > 0:
    config_vals = ""
    with open("config_create_sheets.yaml", "r") \
            as cr:
        config_vals = yaml.full_load(cr)
        n = config_vals['n']

        datetime = date_input
        day_n = datetime - timedelta(days=n)
        a = day_n.strftime('%Y%m%d')
        b = day_n.strftime('%Y-%m-%d')

        RUN1 = {'requests': [
            {'addSheet': {
                'properties': {
                    "sheetId": str(a),
                    "title": '' + str(b) + ''
                }
            }}
        ]}
        request1 = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id1, body=RUN1).execute()
        print(request1)

        RUN2 = {'requests': [
            {'addSheet': {
                'properties': {
                    "sheetId": str(a),
                    "title": '' + str(b) + ''
                }
            }}
        ]}
        request2 = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id2, body=RUN2).execute()
        print(request2)

        config_vals['n'] = n - 1
        with open("config_create_sheets.yaml",
                  "w") as cw:
            yaml.dump(config_vals, cw, default_flow_style=True)

        print("(All Operations - Successfully!)")

        continue

        print("EXIT...")

        break  # exit

# standard sheets package n = 33
