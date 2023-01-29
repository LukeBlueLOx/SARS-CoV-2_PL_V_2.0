from oauth2client.service_account import ServiceAccountCredentials
import gspread
import yaml

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "sars-cov-2-poland.json", scope
)
client = gspread.authorize(credentials)

config_vals = ""
with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
T1 = config_vals['T1']
T2 = config_vals['T2']
T3 = config_vals['T3']
T4 = config_vals['T4']

sheet = client.create(T1)
sheet.share('luke.blue.lox@gmail.com', perm_type='user', role='writer')
sheet = client.list_spreadsheet_files(title=T1)
ID1 = (sheet[0]['id'])
config_vals['ID1'] = ID1
with open("config_create_sheets.yaml",
          "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
print('ID1: ' + ID1)

sheet = client.create(T2)
sheet.share('luke.blue.lox@gmail.com', perm_type='user', role='writer')
sheet = client.list_spreadsheet_files(title=T2)
ID2 = (sheet[0]['id'])
config_vals['ID2'] = ID2
with open("config_create_sheets.yaml",
          "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
print('ID2: ' + ID2)

sheet = client.create(T3)
sheet.share('luke.blue.lox@gmail.com', perm_type='user', role='writer')
sheet = client.list_spreadsheet_files(title=T3)
ID3 = (sheet[0]['id'])
config_vals['ID3'] = ID3
with open("config_create_sheets.yaml",
          "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
print('ID3: ' + ID3)

sheet = client.create(T4)
sheet.share('luke.blue.lox@gmail.com', perm_type='user', role='writer')
sheet = client.list_spreadsheet_files(title=T4)
ID4 = (sheet[0]['id'])
config_vals['ID4'] = ID4
with open("config_create_sheets.yaml",
          "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
print('ID1: ' + ID4)

print("(All Operations - Successfully!)")
