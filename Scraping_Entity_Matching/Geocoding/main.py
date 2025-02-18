import geocoding
import json_handling
import pandas as pd
import os
import time


api_key = "Your API Key"
# keyword_search = ['40 Morland Estate Richmond Road London E8 3EY, Greater London, England',
#  'Stretton Hall Hall Lane Lower Stretton Warrington WA4 4NY, Cheshire, England',
#  '5 Park Street Flat Above Park Street Woodstock OX20 1SJ, Oxfordshire, England',
# 'Upper Lodge Cleeve Hill Kelston Road Bath BA1 9AD, Somerset, England',
#  '12 Ranelagh Road Wellingborough NN8 1HZ, Northamptonshire, England',
#  'White Acre Pound Lane Meonstoke SO32 3NP, Hampshire, England',
#  '862-864 Washwood Heath Road Birmingham B8 2NG, West Midlands, England',
#  '3f, Charter House St. Georges Place Canterbury CT1 1UQ, Kent, England',
#  '12 Hatherley Road Sidcup DA14 4DT, Greater London, England',
#                    '10 Victoria Street Ironville Nottingham NG16 5NB, Derbyshire, England'
#                   ]
#
#
# Read addresses from Excel file
df = pd.read_excel("filename.xlsx")
df["New_full_address"] = df['Croft_name'].astype(str)
keyword_search = df['New_full_address'].tolist()

list_results1 = []
for keyword in keyword_search:
    print(keyword)
    gh = geocoding.extract_lat_lng(keyword, api_key)
    time.sleep(2)
    list_results1.append(gh)

data = {"results": list_results1}
directory = 'tester'  # Name of the folder to save JSON
json_handling.save_json_to_directory(data, directory)

json_files_path = os.path.join(os.getcwd(), directory)
json_handling.convert_json_to_excel(json_files_path)





