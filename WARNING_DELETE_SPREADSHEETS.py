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

ID1 = config_vals['ID1']
ID2 = config_vals['ID2']
ID3 = config_vals['ID3']
ID4 = config_vals['ID4']

sheet1 = client.del_spreadsheet(ID1)
sheet2 = client.del_spreadsheet(ID2)
sheet3 = client.del_spreadsheet(ID3)
sheet4 = client.del_spreadsheet(ID4)
