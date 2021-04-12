import requests
import logging
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from scrape_login import login


import pdb

email = 'xxxxx@yyyyy'
password = '*******'

def navigate(driver, actions, search, flag):


    
    logging.info('Navigating...')
    driver.get('https://www.google.co.jp/')

    # ---pythonを検索
    search_window = driver.find_element_by_name('q')
    search_window.send_keys(search)
    search_window.send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('#tads > div > div > div > div.d5oMvf > a > div.cfxYMc.JfZTW.c4Djg.MUxGbd.v0nnCb').click()

    flag = login(driver, email, password)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located)
    source = driver.find_element_by_id('nav-hamburger-menu')
    source.click()
    time.sleep(2)
    #---targetを指定
    target =driver.find_element_by_id('hmenu-container')

    #--開いたメニューにカーソルを合わせる。
    actions.click_and_hold(source)
    actions.move_to_element(target)
    actions.perform()
    time.sleep(2)
    #---
    
    i = 0
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located)
    time.sleep(3)
    for _ in range(10):
        i += 1
        #ログインした場合
        if flag:
     
            category = driver.find_element_by_css_selector('#hmenu-content > ul.hmenu.hmenu-visible > li:nth-child(14) > a')
        else:
        #ログインしていない場合    
            category = driver.find_element_by_css_selector('#hmenu-content > ul.hmenu.hmenu-visible > li:nth-child(13) > a')
        print(category.text)
        if category.text == 'Kindle 本＆電子書籍リーダー': 
            category.click()
            break
        else:
            time.sleep(3)
            actions.click_and_hold(source)
            actions.move_to_element(target)
            actions.perform()
            time.sleep(3)
            print(True)

    driver.find_element_by_css_selector('#hmenu-content > ul.hmenu.hmenu-visible.hmenu-translateX > li:nth-child(10) > a').click()

    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located)
    driver.find_element_by_css_selector('div:nth-child(2) > a.a-link-normal').click()
    
    return
