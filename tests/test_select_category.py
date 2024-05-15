from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from utilities.driver import Driver


def test_select_category(set_up):

    """Test select product category"""

    driver = Driver().chrome_driver()

    mp = MainPage(driver)  # main_page
    mp.choosing_category_with_driver()