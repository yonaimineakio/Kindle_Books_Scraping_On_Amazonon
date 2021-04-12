import requests
import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


from navigate import navigate
from scrape_unlogin import scrape_content_for_login


from write_to_csv import write_to_csv

flag = False
search = 'amazon'



headers = {'xxxxxxx'}
def main():
 
    driver = Chrome(ChromeDriverManager().install()) 
    actions = ActionChains(driver)
    navigate(driver, actions, search ,flag)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located)
 
    contents = scrape_content_for_login(driver)
    write_to_csv(contents)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()