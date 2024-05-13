import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.laptops_catalog_page import LaptopsCatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from utilities.driver import Driver


def test_select_product(set_up):

    driver = Driver().chrome_driver()

    # lp = LoginPage(driver)  # login_page
    # lp.authorization()

    mp = MainPage(driver)  # main_page
    mp.switch_category()

    lcp = LaptopsCatalogPage(driver) # laptops_catalog_page
    lcp.select_product_1()

    pp = ProductPage(driver) # product_page
    pp.change_parameters()