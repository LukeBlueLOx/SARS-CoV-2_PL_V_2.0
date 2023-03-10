#!/bin/bash

config_vals=$(python3 -c "import yaml; print(yaml.safe_load(open('config_create_sheets.yaml')))")
config=$(echo "$config_vals")
MAIN=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['MAIN'].rstrip('/'))")
CORE=$(echo "$config" | python3 -c "import sys; import yaml; config=yaml.safe_load(sys.stdin); print(config['CORE'].rstrip('/'))")

python3 "$CORE/datawrapper_api_update_external_data.py"
python3 "$CORE/7davrr368_dash_bar_chart.py"
python3 "$CORE/14dsumdvsv_dash_scatterplot.py"
python3 "$CORE/diid368_dash_bar_chart.py"
python3 "$CORE/7ddr_dash_table.py"
python3 "$CORE/favrnd21_dash_bar_chart.py"
python3 "$CORE/7davrivsbdv10k_dash_scatterplot.py"
python3 "$MAIN/import_csv_vd_data_from_zip_file_from_api_od.py"
python3 "$CORE/7davri_14d_dates_slider_dash_choropleth_map.py"
python3 "$CORE/daily_cleaning.py"

