import time

from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):

    url = 'https://www.holodilnik.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = '//span[@class="site-header__search-burger-button"]'
    computer_hardware_link = '/html/body/div[4]/div[3]/div/div[4]/div/div/div/div/div[2]/div[4]/div[2]/div[4]/div/div/div/ul[3]/li[4]'
    category_laptops = '/html/body/div[4]/div[2]/div[1]/div/div[1]/div/div[1]'
    close_banner_button = '//*[@id="popmechanic-form-80468"]/div[3]'
    banner_element = '//*[@id="popmechanic-container-80468"]/div[1]/div[1]'

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_computer_hardware_link(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.computer_hardware_link)))

    def get_category_laptops(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.category_laptops)))

    def get_banner_element(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.banner_element)))

    def get_close_banner_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.close_banner_button)))

    # Actions

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_computer_hardware_link(self):
        self.get_computer_hardware_link().click()
        print("Click computer hardware link")

    def click_category_laptops(self):
        self.get_category_laptops().click()
        print("Click category laptops")

    def click_close_banner_button(self):
        self.get_close_banner_button().click()
        print("Click close banner button")

    # Methods

    def switch_category(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.get_current_url()
        try:
            banner = self.get_banner_element()
            print("Find banner " + banner.text)
            time.sleep(5)
            self.click_close_banner_button()

        except NoSuchElementException as NSEE:
            print(NSEE)
        except TimeoutException as TE:
            print(TE)

        finally:
            self.get_current_url()
            time.sleep(2)
            self.click_catalog_button()
            time.sleep(2)
            self.click_computer_hardware_link()
            time.sleep(2)
            self.get_current_url()
            time.sleep(2)
            self.click_category_laptops()
