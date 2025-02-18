import os
import json
import pandas as pd

def save_json_to_directory(data, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, 'results.json'), 'w') as outfile:
        json.dump(data, outfile)

def convert_json_to_excel(json_files_path):
    json_file_names = [filename for filename in os.listdir(json_files_path) if filename.endswith('.json')]
    if len(json_file_names) == 0:
        print("No JSON files found in the directory.")
        return
    new_df = pd.DataFrame()
    for json_file_name in json_file_names:
        with open(os.path.join(json_files_path, json_file_name)) as json_file:
            json_lists = json.load(json_file)
            for j in range(len(json_lists['results'])):
                if len(json_lists['results'][j]['results']) == 1:
                    tmp = pd.json_normalize(json_lists['results'][j]['results'])
                    new_df = pd.concat([new_df, tmp])
                elif len(json_lists['results'][j]['results']) == 0:
                    new_df = new_df.append(pd.Series(), ignore_index=True)
                else:
                    tmp = pd.json_normalize(json_lists['results'][j]['results'][0])
                    new_df = pd.concat([new_df, tmp])
    if not new_df.empty:
        new_filename = os.path.join(json_files_path, "combined_results.xlsx")
        new_df.to_excel(new_filename, index=False)
        print("Combined results saved to:", new_filename)
    else:
        print("No data to convert.")
