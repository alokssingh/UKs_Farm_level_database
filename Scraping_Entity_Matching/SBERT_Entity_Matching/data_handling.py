import pandas as pd


def load_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df
