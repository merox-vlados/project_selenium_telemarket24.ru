import time

from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage2(Base):

    url = 'https://telemarket24.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    menu = '//*[@id="mm-0"]/div[2]/header/div[2]/div/div/div[1]/div[1]'
    catalog_phone_smartphone = '//*[@id="mm-0"]/div[2]/div[9]/section[2]/div/div/div/a[1]'
    main_word = '//*[@id="catalog-page"]/div/div/div[1]/h1'




    # Getters

    def get_menu(self):
        value_menu = self.driver.find_element(By.XPATH, self.menu)
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of(value_menu))
    def get_catalog_phone_smartphone(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog_phone_smartphone)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))



    # Actions

    def click_menu(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_menu()).perform()
        print('Move menu')

    def click_catalog_phone_smartphone(self):
        self.get_catalog_phone_smartphone().click()
        print("Click category")


    # Methods

    def switch_category(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.get_current_url()
        time.sleep(2)
        self.click_menu()
        # self.driver.maximize_window()
        # self.click_catalog_phone_smartphone()
        # time.sleep(2)
        # self.assert_word(self.get_main_word(),'Телефоны и смартфоны')
        # time.sleep(2)

