import time

from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):

    url = 'https://telemarket24.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_phone_smartphone = '//*[@id="mm-0"]/div[2]/div[9]/section[2]/div/div/div/a[1]'
    main_word = '//*[@id="catalog-page"]/div/div/div[1]/h1'




    # Getters


    def get_catalog_phone_smartphone(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog_phone_smartphone)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))



    # Actions

    def click_catalog_phone_smartphone(self):
        self.get_catalog_phone_smartphone().click()
        print("Click category")


    # Methods

    def switch_category(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        self.click_catalog_phone_smartphone()
        self.assert_word(self.get_main_word(),'Телефоны и смартфоны')



