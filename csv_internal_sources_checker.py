from datetime import datetime
import yaml
import os
import time
import requests

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
Source1 = config_vals['api_daily_data_Source1']
Source2 = config_vals['api_daily_data_Source2']
sep = config_vals['sep']
Source1 = config_vals['Source1']
Source2 = config_vals['Source2']

t = datetime.today().strftime('%Y-%m-%d')
format = "%Y-%m-%d"
t = datetime.strptime(t, format).date()
a = t.strftime('%Y%m%d')

url1 = Source1 + a + '.csv'
url2 = Source2 + a + '.csv'

response1 = requests.head(url1)
if response1.status_code == 200:
    print('The Voivodeships daily yyyymmdd.csv file from API OD exists.')
else:
    print('The Voivodeships daily yyyymmdd.csv file from API OD does not exist.')

response2 = requests.head(url2)
if response2.status_code == 200:
    print('The Districts daily yyyymmdd.csv file from API OD exists.')
else:
    print('The Districts daily yyyymmdd.csv file from API OD does not exist.')
    os.system('python3 /home/blox_land/PycharmProjects/SARS-CoV-2_PL_V2'
              '/import_daily_csv_data_from_api_od.py')
