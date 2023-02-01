#!/bin/bash

config_vals=$(python3 -c "import yaml; print(yaml.safe_load(open('config_create_sheets.yaml')))")
config=$(echo "$config_vals")
MAIN=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['MAIN'].rstrip('/'))")
CORE=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['CORE'].rstrip('/'))")

python3 "$CORE/count_sums.py"
