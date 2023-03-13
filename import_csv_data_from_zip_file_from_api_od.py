from github import Github
import pandas as pd
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from datetime import timedelta
import yaml
import time
import subprocess

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
b = t - timedelta(days=1)
print (b)

url1 = url_source1
url2 = url_source2
script_path1 = ""+str(MAIN)+"startupscript1.sh"
script_path2 = ""+str(MAIN)+"startupscript2.sh"

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
            if 'liczba_nowych_zakazen' not in df1.columns:
                df1.insert(1, column="liczba_nowych_zakazen", value="-")
            if 'liczba_ponownych_zakazen' not in df1.columns:
                df1.insert(2, column="liczba_ponownych_zakazen", value="-")
            if 'liczba_nowych_zakazen_na_10_tys_mieszkancow' not in df1.columns:
                df1.insert(4,
                           column="liczba_nowych_zakazen_na_10_tys_mieszkancow",
                           value="-")
            if 'liczba_ponownych_zakazen_na_10_tys_mieszkancow' not in df1.columns:
                df1.insert(5,
                           column="liczba_ponownych_zakazen_na_10_tys_mieszkancow",
                           value="-")
            if 'liczba_ozdrowiencow' not in df1.columns:
                df1.insert(11, column="liczba_ozdrowiencow", value="-")
            if 'liczba_osob_objetych_kwarantanna' not in df1.columns:
                df1.insert(12, column="liczba_osob_objetych_kwarantanna",value="-")
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
            if 'liczba_nowych_zakazen' not in df2.columns:
                df2.insert(2, column="liczba_nowych_zakazen", value="-")
            if 'liczba_ponownych_zakazen' not in df2.columns:
                df2.insert(3, column="liczba_ponownych_zakazen", value="-")
            if 'liczba_nowych_zakazen_na_10_tys_mieszkancow' not in df2.columns:
                df2.insert(5,
                           column="liczba_nowych_zakazen_na_10_tys_mieszkancow",
                           value="-")
            if 'liczba_ponownych_zakazen_na_10_tys_mieszkancow' not in df2.columns:
                df2.insert(6,
                           column="liczba_ponownych_zakazen_na_10_tys_mieszkancow",
                           value="-")
            if 'liczba_ozdrowiencow' not in df2.columns:
                df2.insert(12, column="liczba_ozdrowiencow", value="-")
            if 'liczba_osob_objetych_kwarantanna' not in df2.columns:
                df1.insert(13, column="liczba_osob_objetych_kwarantanna",
                           value="-")
print(df2.head())

check_date = df2.at[0, 'stan_rekordu_na']
print('"stan_rekordu_na" from source: ' + check_date)
print('Whether: "stan_rekordu_na" from source = "stan_rekordu_na" ???:')

if check_date == str(b):
    print('YES')
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
    time.sleep(15)

    # current_day = t.weekday()
    # if current_day == 6:
    #     result = subprocess.call(['bash', script_path1])
    # else:
    #     result = subprocess.call(['bash', script_path2])
    #
    # nextday1 = t + timedelta(days=1)
    #
    # config_vals['datetime'] = nextday1
    # with open(MAIN + "config_create_sheets.yaml",
    #           "w") as cw:
    #    yaml.dump(config_vals, cw, default_flow_style=True)

else:
    print('NO')
