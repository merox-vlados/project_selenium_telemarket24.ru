from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_select_category(set_up):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    chrome_service = Service('C:/Users/merox/Desktop/QA/resource/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=chrome_service)

    lp = LoginPage(driver) # login_page
    lp.authorization()

    mp = MainPage(driver) # main_page
    mp.switch_category()