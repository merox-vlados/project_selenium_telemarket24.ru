from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage


def test_select_category(set_up):

    path_chromedriver_d = 'D:/QA_Engineer/PyChar/resource/chromedriver.exe'
    path_chromedriver_c = 'C:/Users/merox/Desktop/QA/resource/chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    chrome_service = Service(path_chromedriver_d)
    driver = webdriver.Chrome(options=options, service=chrome_service)

    mp = MainPage(driver) # main_page
    mp.switch_category()