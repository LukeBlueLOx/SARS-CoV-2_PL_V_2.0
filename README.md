# SARS-CoV-2_PL_V_2.0

```
t = datetime.today().strftime('%Y-%m-%d')
format = "%Y-%m-%d"
t = datetime.strptime(t, format).date()
a = t.strftime('%Y%m%d')

config_vals['datetime'] = t
with open(""+str(MAIN)+"config_create_sheets.yaml","w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
```
Finally, the date for the entire project will be saved as an object in the configuration file: config_create_sheets.yaml . I adopted this solution - because the planned version of the application 3.0 provides for manual entry of a specific date in the configuration file: in order to generate data and time series for a given period.

✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌

### https://github.com/LukeBlueLOx/SARS-CoV-2_PL_V_2.0/issues/1
---
