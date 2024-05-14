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

    menu_button = '//*[@id="mm-0"]/div[2]/header/div[2]/div/div/div[1]/div[1]'
    catalog_phone_smartphone = '//*[@id="mm-0"]/div[2]/header/div[2]/div/div/div[1]/div[2]/ul/li[1]/a/span'
    main_word = '//*[@id="catalog-page"]/div/div/div[1]/h1'



    # Getters

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, self.menu_button)))

    def get_catalog_phone_smartphone(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, self.catalog_phone_smartphone)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))



    # Actions

    def click_menu_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_menu_button()).perform()
        print("Move to element menu button")

    def click_catalog_phone_smartphone(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_catalog_phone_smartphone()).click(self.get_catalog_phone_smartphone()).perform()
        print("Click category phone smartphone")


    # Methods

    def choosing_category(self):
        self.get_current_url()
        time.sleep(2)
        self.click_menu_button()
        time.sleep(2)
        self.click_catalog_phone_smartphone()
        time.sleep(2)
        self.assert_word(self.get_main_word(),'Телефоны и смартфоны')
        time.sleep(2)

