import json
import pandas as pd
import os

def json_to_csv(data, filepath):
    df = pd.DataFrame(data)
    if not os.path.isfile(filepath): # If file doesn't exist yet
        df.to_csv(filepath, index=False)
    else: # Only append if file already exists
        df.to_csv(filepath, mode='a', header=False, index=False)
        
def get_data(filepath):
    return pd.read_csv(filepath)