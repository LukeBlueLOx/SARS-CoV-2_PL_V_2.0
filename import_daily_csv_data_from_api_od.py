from github import Github
import pandas as pd
from datetime import datetime, timedelta
import yaml
import time
import subprocess

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']
Source1 = config_vals['api_daily_data_Source1']
Source2 = config_vals['api_daily_data_Source2']
sep = config_vals['sep']
save_path_extract1 = config_vals['save_path_extract1']
save_path_extract2 = config_vals['save_path_extract2']
s = config_vals['g']
g = Github(s)

t = datetime.today().strftime('%Y-%m-%d')
format = "%Y-%m-%d"
t = datetime.strptime(t, format).date()
a = t.strftime('%Y%m%d')
sheet_id1 = a
sheet_id2 = a
b = t - timedelta(days=1)

config_vals['datetime'] = t
with open(""+str(MAIN)+"config_create_sheets.yaml","w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
print('DATE: ' + str(t))
print('"stan_rekordu_na": ' + str(b))
file1 = a + '.csv'
file2 = a + '.csv'
script_path1 = ""+str(MAIN)+"startupscript1.sh"
script_path2 = ""+str(MAIN)+"startupscript2.sh"

df1 = pd.read_csv(Source1, sep=sep, encoding="")
if 'liczba_nowych_zakazen' not in df1.columns:
    df1.insert(1, column="liczba_nowych_zakazen", value="-")
if 'liczba_ponownych_zakazen' not in df1.columns:
    df1.insert(2, column="liczba_ponownych_zakazen", value="-")
if 'liczba_nowych_zakazen_na_10_tys_mieszkancow' not in df1.columns:
    df1.insert(4, column="liczba_nowych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ponownych_zakazen_na_10_tys_mieszkancow' not in df1.columns:
    df1.insert(5, column="liczba_ponownych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ozdrowiencow' not in df1.columns:
    df1.insert(11, column="liczba_ozdrowiencow", value="-")

df2 = pd.read_csv(Source2, sep=sep, encoding="")
if 'liczba_nowych_zakazen' not in df2.columns:
    df2.insert(2, column="liczba_nowych_zakazen", value="-")
if 'liczba_ponownych_zakazen' not in df2.columns:
    df2.insert(3, column="liczba_ponownych_zakazen", value="-")
if 'liczba_nowych_zakazen_na_10_tys_mieszkancow' not in df2.columns:
    df2.insert(5, column="liczba_nowych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ponownych_zakazen_na_10_tys_mieszkancow' not in df2.columns:
    df2.insert(6, column="liczba_ponownych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ozdrowiencow' not in df2.columns:
    df2.insert(12, column="liczba_ozdrowiencow", value="-")

print(df1)
print(df2)
print('Save: ' + save_path_extract1 + file1)
print('Save: ' + save_path_extract2 + file2)

check_date = df2.at[0, 'stan_rekordu_na']
print('"stan_rekordu_na" from source: ' + check_date)
print('Whether: "stan_rekordu_na" from source = "stan_rekordu_na" ???:')

if check_date == str(b):
    print('YES')
    df1.to_csv(save_path_extract1 + (a) + '.csv', index=False)
    df2.to_csv(save_path_extract2 + (a) + '.csv', index=False)

    repo = g.get_user().get_repo("SARS-CoV-2_PL_V_2.0")

    file_path = 'DATA/Source1/'+(a)+'.csv'
    with open(file_path, 'r') as file:
        content = file.read()
    repo.create_file(file_path, "Save: DATA/Source1/"+(a)+".csv",
                     content)

    file_path = 'DATA/Source2/'+(a)+'.csv'
    with open(file_path, 'r') as file:
        content = file.read()
    repo.create_file(file_path, "Save: DATA/Source2/"+(a)+".csv",
                     content)
    time.sleep(15)

    # import datetime
    # current_day = datetime.datetime.today().weekday()
    # if current_day == 6:
    #     result = subprocess.call(['bash', script_path1])
    # else:
    #     result = subprocess.call(['bash', script_path2])

else:
    print('NO')
