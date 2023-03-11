from datetime import timedelta
import yaml
import os
import requests
import subprocess

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
sep = config_vals['sep']
Source4 = config_vals['Source4']
Source5 = config_vals['Source5']

t = config_vals['datetime']
a = t.strftime("%Y%m%d")
print (a)

url1 = Source4 + a + '.csv'
url2 = Source5 + a + '_7DAVRDLR14D.csv'
script_path1 = ""+str(MAIN)+"initial_startupscript1.sh"
script_path2 = ""+str(MAIN)+"initial_startupscript2.sh"
script_path3 = ""+str(MAIN)+"startupscript1.sh"
script_path4 = ""+str(MAIN)+"startupscript2.sh"

response1 = requests.head(url1)
if response1.status_code == 200:
    print('The Districts yyyymmdd.csv file from ZIP API OD exists.')
else:
    print('The Districts yyyymmdd.csv file from ZIP API OD does not exist.')
    os.system('python3 /home/blox_land/PycharmProjects/SARS-CoV-2_PL_V2'
              '/import_csv_data_from_zip_file_from_api_od.py')

response1 = requests.head(url1)
if response1.status_code == 200:
    print('The Districts yyyymmdd.csv file from ZIP API OD exists.')
    current_day = t.weekday()
    if current_day == 6:
        response2 = requests.head(url2)
        if response2.status_code == 200:
            print('The yyyymmdd_7DAVRDLR14D.csv file exists.')
        else:
            print('The yyyymmdd_7DAVRDLR14D.csv file does not exist.')
        result = subprocess.call(['bash', script_path1])
    else:
        response2 = requests.head(url2)
        if response2.status_code == 200:
            print('The yyyymmdd_7DAVRDLR14D.csv file exists.')
        else:
            print('The yyyymmdd_7DAVRDLR14D.csv file does not exist.')
        result = subprocess.call(['bash', script_path2])
else:
    print('The Districts yyyymmdd.csv file from ZIP API OD does not exist.')
    
response1 = requests.head(url1)
if response1.status_code == 200:
    print('The Districts yyyymmdd.csv file from ZIP API OD exists.')
    current_day = t.weekday()
    if current_day == 6:
        response2 = requests.head(url2)
        if response2.status_code == 200:
            print('The yyyymmdd_7DAVRDLR14D.csv file exists.')
            result = subprocess.call(['bash', script_path3])
            nextday1 = t + timedelta(days=1)
            config_vals['datetime'] = nextday1
            with open(MAIN + "config_create_sheets.yaml",
                      "w") as cw:
                yaml.dump(config_vals, cw, default_flow_style=True)
        else:
            print('The yyyymmdd_7DAVRDLR14D.csv file does not exist.')
            result = subprocess.call(['bash', script_path1])
    else:
        response2 = requests.head(url2)
        if response2.status_code == 200:
            print('The yyyymmdd_7DAVRDLR14D.csv file exists.')
            result = subprocess.call(['bash', script_path4])
            nextday1 = t + timedelta(days=1)
            config_vals['datetime'] = nextday1
            with open(MAIN + "config_create_sheets.yaml",
                      "w") as cw:
                yaml.dump(config_vals, cw, default_flow_style=True)
        else:
            print('The yyyymmdd_7DAVRDLR14D.csv file does not exist.')
            result = subprocess.call(['bash', script_path2])
else:
    print('The Districts yyyymmdd.csv file from ZIP API OD does not exist.')
