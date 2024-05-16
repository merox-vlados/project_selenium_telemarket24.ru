import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    """Main page of site """

    url = 'https://telemarket24.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    """Creating locator variables"""

    menu_button = '//*[@id="mm-0"]/div[2]/header/div[2]/div/div/div[1]/div[1]'
    catalog_phone_smartphone = '//*[@id="mm-0"]/div[2]/header/div[2]/div/div/div[1]/div[2]/ul/li[1]/a/span'
    main_word = '//*[@id="catalog-page"]/div/div/div[1]/h1'


    # Getters

    """Get value locators"""

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, self.menu_button)))

    def get_catalog_phone_smartphone(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, self.catalog_phone_smartphone)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))



    # Actions

    """Action with locators"""

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

        with allure.step("Choosing category"):

            """Method chose category"""

            Logger.add_start_step(method='choosing_category')

            self.get_current_url()
            time.sleep(2)
            self.click_menu_button()
            time.sleep(2)
            self.click_catalog_phone_smartphone()
            time.sleep(2)
            self.assert_word(self.get_main_word(),'Телефоны и смартфоны')
            time.sleep(2)

            Logger.add_end_step(url=self.get_current_url(), method='choosing_category')

    def choosing_category_with_driver(self):

        with allure.step("Choosing category with driver"):

            Logger.add_start_step(method='choosing_category_with_driver')

            self.driver.get(self.url)
            time.sleep()
            self.get_current_url()
            time.sleep(2)
            self.click_menu_button()
            time.sleep(2)
            self.click_catalog_phone_smartphone()
            time.sleep(2)
            self.assert_word(self.get_main_word(),'Телефоны и смартфоны')
            time.sleep(2)

            Logger.add_end_step(url=self.get_current_url(), method='choosing_category_with_driver')

