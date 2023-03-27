from datetime import timedelta
import yaml

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
t = config_vals['datetime']

nextday1 = t + timedelta(days=1)
print('Save: ' + str(nextday1) + ' in config_create_sheets.yaml')
config_vals['datetime'] = nextday1
with open(MAIN + "config_create_sheets.yaml",
          "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
