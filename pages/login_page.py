import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.holodilnik.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_icon = '//span[@data-smoke="btn-login__header"]'
    login_link = '//div[contains(text()," Войти по паролю ")]'
    user_name = '//input[@id="controlInput_5"]'
    user_password = '//input[@id="controlInput_6"]'
    login_button = '//button[contains(@class, "button_primary")]'
    login_icon_2 = '/html/body/div[4]/header/div[2]/div[2]/div/div[2]/div[1]/a/span[1]/svg'
    main_word = '/html/body/div[4]/div[2]/div[1]/div/h1'
    close_banner_button = '//*[@id="popmechanic-form-80468"]/div[3]'


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

    def get_login_icon_2(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_icon_2)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_close_banner_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.close_banner_button)))



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

    def click_login_icon_2(self):
        self.get_login_icon_2().click()
        print("Click login icon 2")

    def click_close_banner_button(self):
        self.get_close_banner_button().click()
        print("Click close banner button")



    # Methods

    def authorization(self):
        try:
            self.driver.get(self.url)
            # self.driver.maximize_window()
            self.get_current_url()
            time.sleep(2)
            self.click_login_icon()
            time.sleep(2)
            self.click_login_link()
            time.sleep(2)
            self.input_user_name('merox-vlados@yandex.ru')
            time.sleep(2)
            self.input_user_password('QAholodilnik.ru')
            time.sleep(2)
            self.click_login_button()
            time.sleep(2)
            self.click_login_icon_2()
            time.sleep(2)
            self.assert_word(self.get_main_word(), 'Личный кабинет')
        except TimeoutException as TE:
            self.click_close_banner_button()
        except ElementClickInterceptedException as ECIE:
            self.click_close_banner_button()

