from github import Github
import pandas as pd
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
import yaml
from datetime import timedelta

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
n = config_vals['n']
url_source5 = config_vals['url_source5']
save_path_extract9 = config_vals['save_path_extract9']
s = config_vals['g']
g = Github(s)
t = config_vals['datetime']
a = t.strftime("%Y%m%d")
print (a)

url = url_source5

with urlopen(url) as zip_url:
    with ZipFile(BytesIO(zip_url.read())) as zip_file:
        csv_filename = None
        for name in zip_file.namelist():
            if name.startswith(a) and name.endswith("w_szczepienia.csv"):
                csv_filename = name
                break
        if csv_filename is None:
            raise ValueError("CSV file not found in zip file")
        with zip_file.open(csv_filename, "r") as csv_file:
            df1 = pd.read_csv(csv_file, delimiter=';', encoding="cp1250")
print(df1.head())

df1.to_csv(save_path_extract9 + (a) + '.csv', sep=',', index=False)
repo = g.get_user().get_repo("SARS-CoV-2_PL_V_3.0")

file_path = 'DATA/Vaccinations_D/' + (a) + '.csv'
with open(file_path, 'r') as file:
    content = file.read()
repo.create_file(file_path, "Save: DATA/Vaccinations_D/" + (a) + ".csv",
                    content)
