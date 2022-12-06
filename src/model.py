import gensim.downloader
from gensim.utils import tokenize
import numpy as np
import pandas as pd

def find_slant(in_fpath, out_fpath):
    word_vecs = gensim.downloader.load('glove-wiki-gigaword-100')
    df = pd.read_parquet(in_fpath)

    reference = ['democrat', 'liberal', 'conservative', 'republican']
    for ref in reference:
        def get_score(row):
            scores = []
            for col in ['title', 'tags']:
                text = tokenize(row[col], lower=True)
            for word in text:
                try:
                    scores.append(word_vecs.similarity(word, ref))
                except KeyError:
                    continue
            return np.mean(scores)
        
        df[f'{ref}_similarity'] = df.apply(get_score, axis=1)
        
    df.to_parquet(out_fpath)