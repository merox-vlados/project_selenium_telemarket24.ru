import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from utilities.driver import Driver


def test_authorization(set_up):

    driver = Driver().chrome_driver()

    lp = LoginPage(driver) # login_page
    lp.authorization()

    time.sleep(1)