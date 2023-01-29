import urllib.request
import zipfile
import yaml
import os

config_vals = ""
with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
Source1 = config_vals['url_source1']
Source2 = config_vals['url_source2']
save_path1 = config_vals['save_path1']
save_path2 = config_vals['save_path2']
save_path_extract1 = config_vals['save_path_extract1']
save_path_extract2 = config_vals['save_path_extract2']

urllib.request.urlretrieve(Source1, save_path1)
urllib.request.urlretrieve(Source2, save_path2)

with zipfile.ZipFile(save_path1, 'r') as zip_ref:
    zip_ref.extractall(save_path_extract1)
with zipfile.ZipFile(save_path2, 'r') as zip_ref:
    zip_ref.extractall(save_path_extract2)

path1 = (save_path_extract1)
for i in os.listdir(path1):
    os.rename(os.path.join(path1, i),os.path.join(path1, i[:8])+'.csv')
path2 = (save_path_extract2)
for i in os.listdir(path2):
    os.rename(os.path.join(path2, i),os.path.join(path2, i[:8])+'.csv')
