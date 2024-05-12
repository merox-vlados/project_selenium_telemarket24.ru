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

    # Peremen

    text_banner = "Дарим 1 000 ₽ Давайте дружить? Подпишитесь на наши письма об акциях, обзоры новинок и рейтинги — и мы подарим вам промокод на 1 000 ₽ в первом письме. Подписаться Нажимая «Подписаться», я даю согласие на обработку персональных данных в соответствии c политикой конфиденциальности."


    # Locators

    slider = '//*[@id="value_price"]/span[1]'
    checkbox = '//*[@id="cl_vendor"]/div[4]/div/div/div/div[5]'
    submit_button = '//*[@id="cfilter_btnsubmit"]'
    select_product_button = '//*[@id="view-row"]/div[11]/div/div[2]/div[2]/div/div[1]/div[1]'
    product_add_cart_button = '/html/body/div[4]/div[2]/div/div/div[1]/div[3]/div/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/span[1]'
    go_shopping_cart_button = '//*[@id="modal-product-add-cart-button"]'
    banner_element = '//*[@id="popmechanic-container-80468"]/div[1]/div[1]'
    close_banner_button = '//*[@id="popmechanic-form-80468"]/div[3]'


    # Getters

    def get_slider(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.slider)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_select_product_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.select_product_button)))

    def get_product_add_cart_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_add_cart_button)))

    def get_go_shopping_cart_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.go_shopping_cart_button)))

    def get_banner_element(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.banner_element)))


    def get_close_banner_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.close_banner_button)))




    # Actions

    def move_slider(self):
        slider = self.get_slider()
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(25,0).release().perform()
        print("Move slider")

    def click_checkbox(self):
        # action = ActionChains(self.driver)
        # action.move_to_element(self.get_checkbox()).perform()
        self.get_checkbox().click()
        print("Click checkbox")
    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")

    def click_select_product_button(self):
        self.get_select_product_button().click()
        print("Click product button")
    def click_product_add_cart_button(self):
        self.get_product_add_cart_button().click()
        print("Click product add cart button")

    def click_go_shopping_cart_button(self):
        self.get_go_shopping_cart_button().click()
        print("Click go shopping cart button")

    def click_close_banner_button(self):
        self.get_close_banner_button().click()
        print("Click close banner button")


    # Methods
    def select_product_1(self):

        try:
            banner = self.get_banner_element()
            print("Find banner " + banner.text)
            time.sleep(5)
            self.click_close_banner_button()
        except NoSuchElementException as NSEE:
            print(NSEE.stacktrace)
        except TimeoutException as TE:
            print(TE.stacktrace)
        finally:
            self.get_current_url()
            time.sleep(2)
            self.move_slider()
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 50);")
            time.sleep(2)
            self.click_checkbox()
            time.sleep(2)
            self.click_submit_button()
            time.sleep(2)
            self.click_select_product_button()
            time.sleep(2)
            self.click_product_add_cart_button()
            time.sleep(2)
            self.click_go_shopping_cart_button()


        # except TimeoutException as TE:
        #     self.click_close_banner_button()
        # except ElementClickInterceptedException as ECIE:
        #     self.click_close_banner_button()


