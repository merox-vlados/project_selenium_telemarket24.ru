import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage


def test_authorization(set_up):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    chrome_service = Service('C:/Users/merox/Desktop/QA/resource/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=chrome_service)

    lp = LoginPage(driver) # login_page
    lp.authorization()

    time.sleep(1)