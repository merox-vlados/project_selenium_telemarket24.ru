import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class SmartphonesCatalogPage(Base):

    """Page catalogs phone and smartphones"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    """Creating locator variables"""

    slider = '//*[@id="slider_price_6"]/div[1]/div[1]/div'
    manufacturer_filter = '//*[@id="marka"]/div'
    checkbox = '//*[@id="arrFilter_436_2537327198-styler"]'
    set_filter_button = '//*[@id="set_filter"]'
    main_word = '//*[@id="stiky-title-panel"]/div/div[2]/h1'
    select_product_link = '//*[@id="bx_3966226736_blocks-91274"]/div/div[2]/div[1]/a/span'

    # Getters

    """Get value locators"""

    def get_slider(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.slider)))

    def get_manufacturer_filter(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.manufacturer_filter)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_filter_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.set_filter_button)))

    def get_select_product_link(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_product_link)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions

    """Action with locators"""

    def move_slider(self):
        slider = self.get_slider()
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(25,0).release().perform()
        print("Move slider")

    def click_manufacturer_filter(self):
        self.get_manufacturer_filter().click()
        print("Click manufacturer filter")

    def click_checkbox(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_checkbox()).perform()
        self.get_checkbox().click()
        print("Click checkbox")

    def click_set_filter_button(self):
        self.get_filter_button().click()
        print("Click set filter button")

    def click_select_product_link(self):
        self.get_select_product_link().click()
        print("Click select product link")


    # Methods

    def select_product_1(self):

        with allure.step('select_product_1'):

            """Method filter product page and chose product # 1 """

            Logger.add_start_step(method='select_product_1')

            self.get_current_url()
            time.sleep(2)
            self.assert_url("https://telemarket24.ru/catalog/telefony_i_smartfony/")
            time.sleep(2)
            self.move_slider()
            time.sleep(2)
            self.click_manufacturer_filter()
            time.sleep(2)
            self.click_checkbox()
            time.sleep(2)
            self.click_set_filter_button()
            time.sleep(2)
            self.click_select_product_link()
            time.sleep(2)
            self.assert_word(self.get_main_word(), 'Смартфон ASUS Zenfone 11 Ultra 12/256GB Blue (Синий)')
            time.sleep(2)

            Logger.add_end_step(url=self.get_current_url(), method='select_product_1')




