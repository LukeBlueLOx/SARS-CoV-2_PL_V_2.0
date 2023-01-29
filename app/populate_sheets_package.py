import subprocess
import yaml
from datetime import datetime, timedelta

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
n = config_vals['n']
a = datetime.today() - timedelta(days=n)
t = a.strftime('%Y-%m-%d')
config_vals['datetime'] = t
with open("config_create_sheets.yaml", "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)

while n > 0:
    with open("config_create_sheets.yaml", "r") as cr:
        config_vals = yaml.full_load(cr)
    n = config_vals['n']
    script_path = "startupscript_1.sh"
    t = config_vals['datetime']

    result = subprocess.call(['bash', script_path])

    config_vals['n'] = n - 1
    with open("config_create_sheets.yaml","w") as cw:
        yaml.dump(config_vals, cw, default_flow_style=True)

    a = datetime.today() - timedelta(days=n)
    t = a.strftime('%Y-%m-%d')
    config_vals['datetime'] = t
    with open("config_create_sheets.yaml","w") as cw:
        yaml.dump(config_vals, cw, default_flow_style=True)

    continue
    break
else:
    print("(All Operations - Successfully!)")