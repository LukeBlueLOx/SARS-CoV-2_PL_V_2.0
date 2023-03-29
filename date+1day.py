from datetime import timedelta
import yaml
import os
import requests
import subprocess

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']
Source5 = config_vals['Source5']
t = config_vals['datetime']
a = t.strftime("%Y%m%d")
print (a)
url1 = Source5 + a + '_7DAVRDLR14D.csv'

response1 = requests.head(url1)
if response1.status_code == 200:
    print('The YYYYMMDD_7DAVRDLR14D.csv file from ZIP API OD exists.')

    with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
        config_vals = yaml.full_load(cr)
    t = config_vals['datetime']

    nextday1 = t + timedelta(days=1)
    print('Save: ' + str(nextday1) + ' in config_create_sheets.yaml')
    config_vals['datetime'] = nextday1
    with open(MAIN + "config_create_sheets.yaml",
              "w") as cw:
        yaml.dump(config_vals, cw, default_flow_style=True)

else:
    print('The YYYYMMDD_7DAVRDLR14D.csv file from ZIP API OD does not exist'
          '.')
