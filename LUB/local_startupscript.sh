#! /bin/bash

cd /home/blox_land/PycharmProjects/SARS-CoV-2_PL_V2/
source SARS-CoV-2_PL_V2/bin/activate
python3 csv_internal_sources_from_zip_checker.py
python3 csv_internal_sources_checker.py
