import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    url = 'https://telemarket24.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    """Creating locator variables"""

    main_word = '//*[@id="mm-0"]/div[2]/div[10]/h1'
    name_product = '//span[@data-entity="basket-item-name"]'
    product_price = '//td[@class="basket-items-list-item-price"]/div/div/span'
    total_price = '//*[@id="basket-root"]/div[3]/div/div/div[2]/div/div[2]/div/div'
    place_order_button = '//*[@id="basket-root"]/div[3]/div/div/div[2]/div/div[3]/button'



    # Getters

    """Get value locators"""

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_place_order_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.place_order_button)))


    # Actions

    """Action with locators"""

    def click_place_order_button(self):
        self.get_place_order_button().click()
        print("Click place order button")


    # Methods

    def check_order(self):

        with allure.step("Check order"):

            """Method check order"""

            Logger.add_start_step(method='check_order')

            self.get_current_url()
            time.sleep(1)
            self.assert_url("https://telemarket24.ru/personal/cart/")
            time.sleep(1)
            self.assert_word(self.get_main_word(),'Корзина')
            time.sleep(1)
            self.assert_word(self.get_name_product(), 'Смартфон ASUS Zenfone 11 Ultra 16/512GB Blue (Синий)')
            time.sleep(1)
            self.assert_word(self.get_product_price(), '95 490 ₽')
            time.sleep(1)
            self.assert_word(self.get_total_price(), '95 490 ₽')
            time.sleep(1)
            self.click_place_order_button()
            time.sleep(2)

            Logger.add_end_step(url=self.get_current_url(), method='check_order')



