from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from YTDriver import YTDriver
from utils import list_to_csv
def scrape_video(url):
    """

    Args:
        url (str): Must be a url for a valid YouTube video
    """
    assert('youtube.com' in url.lower())
    
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    elements = driver.find_elements(By.ID, 'video-title')
    out = []
    for elem in elements[:-1]: #Last element is not actually a video
        title = elem.get_attribute('innerHTML').strip()
        link = elem.find_element(By.XPATH, "./../..").get_attribute('href') #Extracts link to video
        
        row = {'title': title, 'link': link, 'source': url}
        out.append(row)
        
    print(out)
    driver.close()
    return out

def scrape_ytdriver(filepath, recursions=5):
    driver = YTDriver(browser='firefox', verbose=True)

    videos = []
    cur_videos = driver.get_homepage()
    if not cur_videos:
        cur_videos = driver.get_homepage()
    videos += cur_videos
    
    for _ in range(recursions):
        driver.play(cur_videos[0], 10)

        cur_videos = driver.get_recommendations()
        videos += cur_videos
            
    driver.close()

    video_urls = [video.url for video in videos]
    video_urls.insert(0, 'https://www.youtube.com') #Demark start of sessions
    
    list_to_csv(video_urls, filepath)
    return video_urls