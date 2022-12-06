from utils import Video
import pandas as pd
import utils

def get_metadata(url):
    v = Video(None, url)
    v.get_metadata()
    row = {'url': url,
        'title': v.metadata['title'],
        'tags': v.metadata['tags'],
        'description': v.metadata['description']}
    return row

def preprocess(in_fpath, out_fpath, steps):
    df = pd.read_csv(in_fpath)
    try:
        out_df = pd.read_parquet(out_fpath)
    except:
        out_df = None
    
    rows = []
    for url in df['url'].values:
        if out_df is not None and url in out_df['url'].values:
            continue
        if url != 'https://www.youtube.com' and url != 'https://www.youtube.com/':
            rows.append(get_metadata(url))
        if len(rows) > steps:
            break
    utils.json_to_parquet(rows, out_fpath)