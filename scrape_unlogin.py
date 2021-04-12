import logging
import time
import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
import pdb

def scrape_content_for_unlogin(driver):
    
    logging.info('scraping.....')
    contents = []

    for book in driver.find_elements_by_css_selector('#browse-grid-view > div'):
        title = book.find_element_by_css_selector('li > span > div > span > a > div').text
        price = book.find_element_by_css_selector('span.p13n-sc-price').text
        try:
            popular = book.find_element_by_css_selector('#zg-ordered-list > li > span > div > span > div.a-icon-row.a-spacing-none > a.a-size-small.a-link-normal').text
        except:
            popular = '評価無し'

        contents.append({
            'title':title,
            'price':price,
            'popular':popular,
        })
    logging.info(f'scraped {len(contents)} data')

    return contents

def scrape_content_for_login(driver):
    i = 0
    logging.info('scraping.....')
    contents = []
    # pdb.set_trace()
    for book in driver.find_elements_by_css_selector('#browse-grid-view > div > a'):
        title = re.search(r'(.*)\n', book.text).group(1)
        price = re.search(r'￥\s([\d,]*)', book.text).group(1)
        like = re.search(r'\n\((.+)\)\n', book.text).group(1)
        
    

        contents.append({
            'title':title,
            'price':price,
            'popular':like,
        })
        i = i + 1
  
    logging.info(f'scraped {len(contents)} data')
    return contents

