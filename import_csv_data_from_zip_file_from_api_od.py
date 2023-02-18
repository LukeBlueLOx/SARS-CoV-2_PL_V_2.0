from github import Github
import pandas as pd
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
import yaml

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
url_source1 = config_vals['url_source1']
url_source2 = config_vals['url_source2']
save_path_extract7 = config_vals['save_path_extract7']
save_path_extract8 = config_vals['save_path_extract8']
s = config_vals['g']
g = Github(s)
t = config_vals['datetime']
a = t.strftime("%Y%m%d")
print (a)

url1 = url_source1
url2 = url_source2

with urlopen(url1) as zip_url:
    with ZipFile(BytesIO(zip_url.read())) as zip_file:
        csv_filename = None
        for name in zip_file.namelist():
            if name.startswith(a) and name.endswith(".csv"):
                csv_filename = name
                break
        if csv_filename is None:
            raise ValueError("CSV file not found in zip file")
        with zip_file.open(csv_filename, "r") as csv_file:
            df1 = pd.read_csv(csv_file, delimiter=';', encoding="cp1250")
print(df1.head())

with urlopen(url2) as zip_url:
    with ZipFile(BytesIO(zip_url.read())) as zip_file:
        csv_filename = None
        for name in zip_file.namelist():
            if name.startswith(a) and name.endswith(".csv"):
                csv_filename = name
                break
        if csv_filename is None:
            raise ValueError("CSV file not found in zip file")
        with zip_file.open(csv_filename, "r") as csv_file:
            df2 = pd.read_csv(csv_file, delimiter=';', encoding="cp1250")
print(df2.head())

df1.to_csv(save_path_extract7 + (a) + '.csv', sep=',', index=False)
df2.to_csv(save_path_extract8 + (a) + '.csv', sep=',', index=False)

repo = g.get_user().get_repo("SARS-CoV-2_PL_V_2.0")

file_path = 'DATA/Source1_From_ZIP/' + (a) + '.csv'
with open(file_path, 'r') as file:
    content = file.read()
repo.create_file(file_path, "Save: DATA/Source1_From_ZIP/" + (a) + ".csv",
                 content)

file_path = 'DATA/Source2_From_ZIP/' + (a) + '.csv'
with open(file_path, 'r') as file:
    content = file.read()
repo.create_file(file_path, "Save: DATA/Source2_From_ZIP/" + (a) + ".csv",
                 content)
