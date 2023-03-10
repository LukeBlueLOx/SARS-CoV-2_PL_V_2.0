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
# python3 "$CORE/7davrr368_dash_bar_chart.py"
# python3 "$CORE/14dsumdvsv_dash_scatterplot.py"
# python3 "$CORE/diid368_dash_bar_chart.py"
# python3 "$CORE/7ddr_dash_table.py"
# python3 "$CORE/favrnd21_dash_bar_chart.py"
# python3 "$CORE/7davrivsbdv10k_dash_scatterplot.py"
# python3 "$CORE/sunday_update/add_weekly_sheets_set.py"
# python3 "$CORE/sunday_update/update_avr7d_array_range_7d.py"
# python3 "$CORE/daily_cleaning.py"
# python3 "$CORE/datawrapper_api_republish_set_for_vacination_booster.py"
# python3 "$MAIN/import_csv_data_from_zip_file_from_api_od.py"
# python3 "$MAIN/import_csv_vd_data_from_zip_file_from_api_od.py"
# python3 "$CORE/7davri_dash_choropleth_map.py"
# python3 "$CORE/bdv_dash_choropleth_map.py"
# python3 "$CORE/v_dash_choropleth_map.py"
# python3 "$CORE/7davri_14d_dates_slider_dash_choropleth_map.py"
# python3 "$CORE/vm_dash_choropleth_map.py"
# python3 "$MAIN/ts_import_csv_data_from_zip_file_from_api_od.py"
# python3 "$MAIN/prepare_vd_data_sources.py"
# python3 "$MAIN/test.py"
