#!/usr/bin/env python

import sys
import os
import json

sys.path.insert(0, 'src')

import utils
from scrape import scrape_video, scrape_ytdriver
import preprocess
import model

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'test' in targets:
        with open('config/test-params.json') as fh:
            test_cfg = json.load(fh)

        #Many parts involving scraping and YouTube recommendations are difficult
        #to test and can't be tested deterministically.
        
        #This tests the main pipeline the scraped data runs through to determine
        #the political slant of videos.
        model.find_slant(**test_cfg)
        
    if 'scrape' in targets:
        with open('config/scrape-params.json') as fh:
            scrape_cfg = json.load(fh)

        data = scrape_video(**scrape_cfg)
        
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
            
        utils.json_to_csv(data, **data_cfg)

    if 'scrape_many' in targets:
        with open('config/scrape-many-params.json') as fh:
            scrape_cfg = json.load(fh)
            
        data = scrape_ytdriver(**scrape_cfg)
        
    if 'preprocess' in targets:
        with open('config/preprocess.json') as fh:
            preproc_cfg = json.load(fh)
        preprocess.preprocess(**preproc_cfg)
        
    if 'model' in targets:
        with open('config/model.json') as fh:
            model_cfg = json.load(fh)
        model.find_slant(**model_cfg)
        
    return

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)