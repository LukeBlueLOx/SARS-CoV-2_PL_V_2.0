#!/bin/bash

config_vals=$(python3 -c "import yaml; print(yaml.safe_load(open('config_create_sheets.yaml')))")
config=$(echo "$config_vals")
MAIN=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['MAIN'].rstrip('/'))")
CORE=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['CORE'].rstrip('/'))")

python3 "$CORE/sunday_update/import_csv_vd_data_from_url.py"
python3 "$CORE/import_csv_data_from_urls.py"
python3 "$CORE/count_sums.py"
python3 "$CORE/iotr.py"
python3 "$CORE/7davrdlr14d.py"