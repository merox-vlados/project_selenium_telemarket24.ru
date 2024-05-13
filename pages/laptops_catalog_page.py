import time

from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class LaptopsCatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




    # Locators

    slider = '//*[@id="slider_price_6"]/div[1]/div[1]/div'
    manufacturer_filter = '//*[@id="marka"]/div'
    checkbox = '//*[@id="arrFilter_436_2537327198-styler"]'
    set_filter_button = '//*[@id="set_filter"]'
    main_word = '//*[@id="stiky-title-panel"]/div/div[2]/h1'



    select_product_link = '//*[@id="bx_3966226736_blocks-91274"]/div/div[2]/div[1]/a/span'


    product_add_cart_button = '/html/body/div[4]/div[2]/div/div/div[1]/div[3]/div/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/span[1]'
    go_shopping_cart_button = '//*[@id="modal-product-add-cart-button"]'

    banner_element = '//*[@id="popmechanic-container-80468"]/div[1]/div[1]'
    close_banner_button = '//*[@id="popmechanic-form-80468"]/div[3]'


    # Getters

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
        self.move_slider()
        self.click_manufacturer_filter()
        self.click_checkbox()
        time.sleep(2)
        self.click_set_filter_button()
        self.click_select_product_link()
        self.assert_word(self.get_main_word(), 'Смартфон ASUS Zenfone 11 Ultra 12/256GB Blue (Синий)')




