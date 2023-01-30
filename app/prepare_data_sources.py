from datetime import timedelta
import pandas as pd
import yaml

config_vals = ""
with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
n = config_vals['n']
Source1 = config_vals['Source1']
Source2 = config_vals['Source2']
sep = config_vals['sep']
datetime = config_vals['datetime']
save_path_extract1 = config_vals['save_path_extract1']
save_path_extract2 = config_vals['save_path_extract2']
print(datetime)

while n > 0:
    config_vals = ""
    with open("config_create_sheets.yaml", "r") \
            as cr:
        config_vals = yaml.full_load(cr)
        n = config_vals['n']

        day_n = datetime - timedelta(days=n)
        a = day_n.strftime('%Y%m%d')
        print(a)

        df1 = pd.read_csv(Source1+(a)+'.csv', sep=sep, encoding="")
        df2 = pd.read_csv(Source2+(a)+'.csv', sep=sep, encoding="")
        print(df1)
        print(df2)

        df1.to_csv(save_path_extract1+(a)+'.csv', index=False)
        df2.to_csv(save_path_extract2+(a)+'.csv', index=False)

        config_vals['n'] = n - 1
        with open("config_create_sheets.yaml",
                  "w") as cw:
            yaml.dump(config_vals, cw, default_flow_style=True)

        continue

        print("EXIT...")

        break  # exit






