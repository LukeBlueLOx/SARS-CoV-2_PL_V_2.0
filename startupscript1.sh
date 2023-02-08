#!/bin/bash

config_vals=$(python3 -c "import yaml; print(yaml.safe_load(open('config_create_sheets.yaml')))")
config=$(echo "$config_vals")
MAIN=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['MAIN'].rstrip('/'))")
CORE=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['CORE'].rstrip('/'))")

# python3 "$CORE/import_csv_data_from_urls.py"
# python3 "$CORE/count_sums.py"
# python3 "$CORE/iotr.py"
# python3 "$CORE/7davrdlr14d.py"
# python3 "$CORE/datawrapper_api_update_external_data.py"
python3 "$CORE/7davrr368_dash_bar_chart.py"
# python3 "$CORE/14dsumdvsv_dash_scatterplot.py"
# python3 "$CORE/sunday_update/add_weekly_sheets_set.py"
# python3 "$CORE/sunday_update/update_avr7d_array_range_7d.py"
