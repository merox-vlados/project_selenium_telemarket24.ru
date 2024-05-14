import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class LoginPage(Base):

    url = "https://telemarket24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_icon = '//*[@id="account-menu-toggler"]/span'
    login_link = '//*[@id="account-menu-toggler"]/span/span/a'
    user_name = '//*[@id="modal_login"]/div/div/div[3]/form/label[1]/input'
    user_password = '//*[@id="USER_PASSWORD"]'
    login_button = '//*[@id="modal_login"]/div/div/div[3]/form/div/div[3]/button'
    main_word = '//*[@id="account-menu-toggler"]/span/span/div/ul/li[2]/a/span'


    # Getters

    def get_login_icon(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_icon)))

    def get_login_link(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_link)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_button)))


    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))



    # Actions

    def click_login_icon(self):
        self.get_login_icon().click()
        print("Click login icon")
    def click_login_link(self):
        self.get_login_link().click()
        print("Click login link")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        print("Input user password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")


    # Methods

    def authorization(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.get_current_url()
        time.sleep(2)
        self.click_login_icon()
        time.sleep(2)
        self.click_login_link()
        time.sleep(2)
        self.input_user_name('qa.godenko@gmail.com')
        time.sleep(2)
        self.input_user_password('QAtelemarket24.ru')
        time.sleep(2)
        self.click_login_button()
        time.sleep(2)
        self.click_login_icon()
        time.sleep(2)
        self.assert_word(self.get_main_word(), 'Мой кабинет')


