---
### SARS-CoV-2_PL_V_2.0
---
#### EN version on GitHub: https://scv2pl.github.io/scv2pl-en
#### EN version on HEROKU: https://blox-land.herokuapp.com/scv2pl_en
#### PL version on GitHub: https://scv2pl.github.io
---
#### Google Sheets For This Project:
* [Voivodeships-V2](https://docs.google.com/spreadsheets/d/1eoLEeidp72jUeAPwfDUKHBJs9OHx7f0PO3cmj3aFBEA/edit?pli=1#gid=0)
* [Districts-V2](https://docs.google.com/spreadsheets/d/1R9gfgth7XGm1Z5A2IStYVoxpNej1balmDsODyU5-ljU/edit#gid=0)
* [Computable-V2](https://docs.google.com/spreadsheets/d/17rIcj6djv7NmIC3RV16VGVkv7tTJgUd8UGvk8ruMOmU/edit?pli=1#gid=0)
* [Data-V2](https://docs.google.com/spreadsheets/d/12rDOluh8jReO5Ss-YqrM1eUIpZLF0zHpxyt9n84TkWU)
---
The daily update of data on the SARS-CoV-2 virus in Poland usually takes place at 10:30AM GMT +0100 CEST local time for Warsaw.

[Government Infection Report](https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2)

Data sources from the API Polish Government [Open Data](https://dane.gov.pl/en) Project:
* [Source1 For Voivodeships](https://api.dane.gov.pl/resources/33193,archiwalne-dane-dla-wojewodztw/file)
* [Source2 For Districts](https://api.dane.gov.pl/resources/33194,archiwalne-dane-dla-powiatow/file)

When a failure occurs - the data can be updated later in the day, or be available only in the following days for download in a zip package. The "SARS-CoV-2_PL_V_2.0" version of the "EPIDEMIA" application is prepared for this and to complete the missing time series - it currently requires manually entering the required configurations and launches until the continuity of time series is obtained. In the near future, this process will be fully automated during a data source failure.

---

The application is originally designed to run automatically in the HEROKU cloud according to the "[Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler)" to execute the file: [import_daily_csv_data_from_api_od.py](https://github.com/LukeBlueLOx/SARS-CoV-2_PL_V_2.0/blob/main/import_daily_csv_data_from_api_od.py) at 11AM GMT +0100 CEST - it is also possible to perform the same process automatically locally using the CRON scheduler. 

Both processes require pre-setting appropriate paths in the configuration file: [config_create_sheets.yaml](https://github.com/LukeBlueLOx/SARS-CoV-2_PL_V_2.0/blob/main/config_create_sheets.yaml)

For HEROKU:
* ```MAIN: /app/,```
* ```CORE: /app/CORE/,```

For Local Environment:
* ```MAIN: /home/blox_land/SARS-CoV-2_PL_V_2.0/,```
* ```CORE: /home/blox_land/SARS-CoV-2_PL_V_2.0/CORE/,```

The LUB folder should be placed in the main directory ```/home/blox_land/```.

With the ```crontab -e``` command in terminal, we run the CRON scheduler and place the contents of the crontab file in it:

```
#! /bin/bash

30 11 * * 0 /home/blox_land/LUB/LUB.sh
00 11 * * * /home/blox_land/LUB/local_startupscript.sh

# $ crontab -e
```

Each *.sh file must be granted permissions: ```chmod +x *.sh```

---

"EPIDEMIA" application version: "SARS-CoV-2_PL_V_2.0" - is a solid, designed foundation for version 3.0, which will be implemented in the near future. The "EPIDEMIA" application in version 3.0 - will be able to generate and visualize time series presented in the "SARS-CoV-2_PL_V_2.0" version for a given date entered by the user.

Python files responsible for generating Plotly - Dash charts are under construction and testing. They will be made available only after the application version 3.0 is completed - together with the availability of the entire application under the appropriate Open Source license. The 3.0 application will rely solely on visualizations generated with Python in Plotly-Dash. Only the Pandas library will be used to generate the datasets - Google Sheets will be the perfect schematic diagram for this task - which is a challenge for me as I am still learning all these new things. Google Sheets will remain in use all the time for applications in version 2.0 - because they are also a great tool and an integral part of the application for daily updating, learning and discovering new solutions.

---

The application in version [1.0 - SCV2PL](https://github.com/SCV2PL/SCV2PL.GitHub.IO) was also adapted to work in Google Cloud Platform when I had free credits to use. The Virtual Machine Computing Engine for the daily update was started and stop using the CRON "Cloud Scheduler" and the function: [GCP](https://github.com/SCV2PL/SCV2PL.GitHub.IO/tree/main/GCP).

---
