#!/bin/bash

config_vals=$(python3 -c "import yaml; print(yaml.safe_load(open('config_create_sheets.yaml')))")
MAIN=$(echo $config_vals | python3 -c "import sys; config=eval(sys.stdin.read()); print(config['MAIN'])")
CORE=$(echo $config_vals | python3 -c "import sys; config=eval(sys.stdin.read()); print(config['CORE'])")

python3 "$CORE/import_csv_data_from_urls.py"
