#! /bin/bash

cd /home/blox_land/PycharmProjects/SARS-CoV-2_PL_V2/
source SARS-CoV-2_PL_V2/bin/activate
python3 import_csv_data_from_zip_file_from_api_od.py
python3 python3 csv_internal_sources_checker.py
