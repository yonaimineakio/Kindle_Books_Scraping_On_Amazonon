import logging
import time
from selenium.webdriver import Chrome, ChromeOptions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


def login(driver, email, psward):
    element = driver.find_element_by_css_selector('.nav-action-inner')
    #JavaScriptを呼びだして無理やりクリック
    driver.execute_script('arguments[0].click();', element)

    element = driver.find_element_by_id('ap_email')
    element.send_keys(email)
    driver.find_element_by_id('continue').click()

    element = driver.find_element_by_id('ap_password')
    element.send_keys(psward)

    driver.find_element_by_id('signInSubmit').click()
    driver.execute_script('window.alert("この後携帯に送られる認証リンクをクリックしてください。");', element)
    time.sleep(10)
    return True
