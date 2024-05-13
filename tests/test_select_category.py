from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from pages.main_page_2 import MainPage2
from utilities.driver import Driver


def test_select_category(set_up):

    driver = Driver().chrome_driver()

    # mp = MainPage(driver) # main_page
    # mp.switch_category()

    mp = MainPage2(driver)  # main_page
    mp.switch_category()