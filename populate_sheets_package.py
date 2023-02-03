import subprocess
import yaml
from datetime import datetime, timedelta

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
n = config_vals['n']
t = datetime.today() - timedelta(days=n)
a = t.strftime('%Y-%m-%d')
format = "%Y-%m-%d"
t = datetime.strptime(a, format).date()
print(t)
config_vals['datetime'] = t
with open("" + str(MAIN) + "config_create_sheets.yaml", "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)

while n > 0:
    with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
        config_vals = yaml.full_load(cr)
    n = config_vals['n']

    script_path = "" + str(MAIN) + "startupscript1.sh"
    result = subprocess.call(['bash', script_path])

    config_vals['n'] = n - 1
    with open(""+str(MAIN)+"config_create_sheets.yaml", "w") as cw:
        yaml.dump(config_vals, cw, default_flow_style=True)

    with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
        config_vals = yaml.full_load(cr)
    n = config_vals['n']

    t = datetime.today() - timedelta(days=n)
    a = t.strftime('%Y-%m-%d')
    format = "%Y-%m-%d"
    t = datetime.strptime(a, format).date()
    print(t)
    config_vals['datetime'] = t
    with open(""+str(MAIN)+"config_create_sheets.yaml", "w") as cw:
        yaml.dump(config_vals, cw, default_flow_style=True)

    continue
    break