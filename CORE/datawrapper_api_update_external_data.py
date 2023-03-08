# from datetime import timedelta
from datawrapper import Datawrapper
import yaml
# import pandas as pd

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
datawrapper_token = config_vals['datawrapper_token']
t = config_vals['datetime']
url_source4 = config_vals['url_source4']
save_path_extract3 = config_vals['save_path_extract3']
save_path_extract4 = config_vals['save_path_extract4']
save_path_extract5 = config_vals['save_path_extract5']

tt = t.strftime('%Y%m%d')
# datetime = t
# print(datetime)
# a = datetime - timedelta(days=1)
# t1 = a.strftime('%Y%m%d')
# b = datetime - timedelta(days=2)
# t2 = b.strftime('%Y%m%d')
# c = datetime - timedelta(days=3)
# t3 = c.strftime('%Y%m%d')
# d = datetime - timedelta(days=4)
# t4 = d.strftime('%Y%m%d')
# e = datetime - timedelta(days=5)
# t5 = e.strftime('%Y%m%d')
# f = datetime - timedelta(days=6)
# t6 = f.strftime('%Y%m%d')
# g = datetime - timedelta(days=7)
# t7 = g.strftime('%Y%m%d')

# df = pd.read_csv(url_source4 + save_path_extract3 + tt + '_SUM.csv', sep=",",
#                  encoding="")
# Infections = df.at[0, '7D AVR Infections / 10000']
# Booster = df.at[0, '(% ) Booster Dose']
# print(Infections)
# print(Booster)
#
# print(tt)
# print(t1)
# print(t2)
# print(t3)
# print(t4)
# print(t5)
# print(t6)
# print(t7)

dw = Datawrapper(access_token = datawrapper_token)

dw_id = 'yUSUL'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = '6HKut'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = 'JW5zN'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = 'p1M7c'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = 'wt85J'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = 'WVcSA'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = 'uO9JC'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = 'C3dh5'
external_data = url_source4 + save_path_extract4 + tt + '_IOTR.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

# dw_id = 'No277'
# external_data = url_source4 + save_path_extract3 + tt + '_SUM.csv'
# print(external_data)
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'FJtlg'
# external_data = url_source4 + save_path_extract3 + tt + '_SUM.csv'
# print(external_data)
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'qGF2F'
# external_data = url_source4 + save_path_extract3 + tt + '_SUM.csv'
# print(external_data)
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = 'gRs82'
# external_data = url_source4 + save_path_extract3 + tt + '_SUM.csv'
# print(external_data)
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'qGF2F'
# highlight_ranges = [
#     [str(Booster), 0, str(Booster), 9.5],
#     [35, str(Infections), 75, str(Infections)]
# ]
# highlight_ranges_string = '\n'.join([','.join([str(x) for x in line]) for line
#                                      in highlight_ranges])
# metadata = {
#     "visualize": {
#         "highlight-range": highlight_ranges_string
#     }
# }
# dw.update_metadata(dw_id, metadata)
#
# dw_id = 'gRs82'
# highlight_ranges = [
#     [str(Booster), 0, str(Booster), 9.5],
#     [35, str(Infections), 75, str(Infections)]
# ]
# highlight_ranges_string = '\n'.join([','.join([str(x) for x in line]) for line
#                                      in highlight_ranges])
# metadata = {
#     "visualize": {
#         "highlight-range": highlight_ranges_string
#     }
# }
# dw.update_metadata(dw_id, metadata)

dw_id = '4nqZF'
external_data = url_source4 + save_path_extract5 + tt + '_7DAVRDLR14D.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

dw_id = 'j0TYA'
external_data = url_source4 + save_path_extract5 + tt + '_7DAVRDLR14D.csv'
print(external_data)
metadata = {
    "data": {
        "external-data": external_data
    }
}
dw.update_metadata(dw_id, metadata)
properties = dw.chart_properties(dw_id)
dw.publish_chart(dw_id)

# dw_id = 'nK681'
# external_data = url_source4 + save_path_extract3 + t1 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'ZJF26'
# external_data =  url_source4 + save_path_extract3 + t2 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'FwfK3'
# external_data = url_source4 + save_path_extract3 + t3 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = 'omUrz'
# external_data =  url_source4 + save_path_extract3 + t4 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = '1cfR3'
# external_data = url_source4 + save_path_extract3 + t5 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = 'galdz'
# external_data = url_source4 + save_path_extract3 + t6 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = '23zkY'
# external_data = url_source4 + save_path_extract3 + t7 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = '3btH7'
# external_data = url_source4 + save_path_extract3 + t1 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'zRe7S'
# external_data = url_source4 + save_path_extract3 + t2 + '_SUM.csv'
# metadata = {
#
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = 'YTJUM'
# external_data =  url_source4 + save_path_extract3 + t3 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'EnedJ'
# external_data =  url_source4 + save_path_extract3 + t4 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = '2rIZu'
# external_data = url_source4 + save_path_extract3 + t5 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)

# dw_id = 'msk23'
# external_data = url_source4 + save_path_extract3 + t6 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = 'KNHOM'
# external_data = url_source4 + save_path_extract3 + t7 + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = 'K8Lky'
# external_data = url_source4 + save_path_extract3 + tt + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
#
# dw_id = 'Il57Q'
# external_data = url_source4 + save_path_extract3 + tt + '_SUM.csv'
# metadata = {
#     "data": {
#         "external-data": external_data
#     }
# }
# dw.update_metadata(dw_id, metadata)
# properties = dw.chart_properties(dw_id)
# dw.publish_chart(dw_id)
