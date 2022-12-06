# DSC180-Project-1

## Running the project

* To install the dependencies, run the following command from the root directory of the project: `pip install -r requirements.txt`
* If scraping, download a Selenium webdriver for your preferred browser (ex: https://github.com/mozilla/geckodriver/releases)
* If gathering video metadata from scraped videos, install youtube-dl to your PATH: https://youtube-dl.org/

## Data:
The process of scraping is an integral part of this project. While the data cannot be downloaded, code for scraping and acquiring data is included and can be run after setting up dependencies.

* Edit __config/scrape-many-params.json__ to set how many recursions deep into YouTube recommendations to scrape.
* Run `python run.py scrape_many` to scrape.
  
### Building the project stages using `run.py`

* After scraping, run `python run.py preprocess`
  - This uses youtube-dl to fetch metadata for all videos scraped.
* To get the results of word2vec models, from the project root dir, run `python run.py model`
  - This uses a pretrained word2vec model to estimate the political slant of videos scraped. Different pretrained models can be specified in __config/model.json__
* To run tests, run `python run.py test`