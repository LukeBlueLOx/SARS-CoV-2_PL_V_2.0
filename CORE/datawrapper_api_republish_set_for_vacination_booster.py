from datawrapper import Datawrapper
import yaml

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']


with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
datawrapper_token = config_vals['datawrapper_token']
dw = Datawrapper(access_token = datawrapper_token)

dw_id = 'EBztU'
dw.publish_chart(dw_id)

# dw_id = 'VFe7U'
# dw.publish_chart(dw_id)

dw_id = 'ogppd'
dw.publish_chart(dw_id)

# dw_id = 'uXBbj'
# dw.publish_chart(dw_id)
