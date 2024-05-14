import time

from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class ProductPage(Base):

    url = 'https://telemarket24.ru/produ%D1%81ts/smartfon_asus_zenfone_11_ultra_16_512gb_blue_siniy.html'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_color_product = '//*[@id="bx_117848907_91274"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/a[1]/img'
    select_ram_product = '//*[@id="bx_117848907_91273"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/a[2]/div'
    value_ram_product = '//*[@id="bx_117848907_91275"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/a[2]/div'
    main_word = '//*[@id="bx_117848907_91275"]/div[2]/div[1]/div[2]/div[3]/div[2]/dl/dd[5]'
    add_product_cart = '//button[@id="bx_117848907_91275_buy_link"]'
    cart_button = '//div[@id="basket"]'
    set_order_button = '//*[@id="popup_basket"]/div[3]/div/a'



    # Getters


    def get_color_product(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_color_product)))

    def get_ram_product(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_ram_product)))

    def get_value_ram_product(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.value_ram_product)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_add_product_cart(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.add_product_cart)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_set_order_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.set_order_button)))



    # Actions

    def click_select_color_product(self):
        self.get_color_product().click()
        print("Click color product")

    def click_select_ram_product(self):
        self.get_ram_product().click()
        print("Click RAM product")

    def click_add_product_cart(self):
        self.get_add_product_cart().click()
        print("Click add product cart")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def click_set_order_button(self):
        self.get_set_order_button().click()
        print("Click set order button")


    # Methods

    def change_parameters_and_select_product(self):
        self.get_current_url()
        time.sleep(2)
        self.click_select_color_product()
        time.sleep(2)
        self.click_select_ram_product()
        time.sleep(2)
        self.assert_word(self.get_main_word(), self.get_value_ram_product().text)
        time.sleep(2)
        self.click_add_product_cart()
        time.sleep(2)
        self.click_cart_button()
        time.sleep(2)
        self.click_set_order_button()
        time.sleep(2)

    def select_product(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.click_add_product_cart()
        time.sleep(2)
        self.click_cart_button()
        time.sleep(2)
        self.click_set_order_button()
        time.sleep(2)


