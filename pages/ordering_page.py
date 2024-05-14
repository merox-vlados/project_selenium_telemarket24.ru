import time

from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class OrderingPage(Base):

    url = 'https://telemarket24.ru/personal/order/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    radio_button = '//*[@id="bx-soa-region"]/div[2]/div[2]/div/div[1]/div[1]'
    address_field = '//input[@class="bx-ui-sls-fake"]'
    address_field_help = '//div[@class="dropdown-item bx-ui-sls-variant bx-ui-sls-variant-active"]'
    next_button_region = '//*[@id="bx-soa-region"]/div[2]/div[3]/div/a'

    payment_checkbox = '//*[@id="bx-soa-paysystem"]/div[2]/div[2]/div[1]/div[2]'
    next_button_payment = '//*[@id="bx-soa-paysystem"]/div[2]/div[4]/div/a[2]'

    delivery_button = '//div[@id="delivery83"]'
    next_button_delivery = '//*[@id="bx-soa-delivery"]/div[2]/div[3]/div/a[2]'

    field_client_name = '//input[@id="soa-property-1"]'
    field_email = '//input[@id="soa-property-3"]'
    field_phone_number = '//input[@id="soa-property-2"]'
    next_button_client_info = '//*[@id="bx-soa-properties"]/div[2]/div[3]/div/a[2]'

    name_product = '//*[@id="bx-soa-basket"]/div[2]/div/div/div/div/div[1]/div/div[2]/div/a'
    price_product = '//*[@id="bx-soa-basket"]/div[2]/div/div/div/div/div[3]/div[2]/strong/span[1]'

    back_main_page_button = '//*[@id="mm-0"]/div[2]/header/div[1]/div/div[2]'
    main_word_main_page = '//*[@id="mm-0"]/div[2]/div[9]/section[2]/div/h1'

    cart_button_main_page = '//div[@id="basket"]'
    clear_basket_button = '//*[@id="popup_basket"]/div[3]/button/span'


    # Getters

    def get_radion_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.radio_button)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_address_field_help(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.address_field_help)))

    def get_next_button_region(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.next_button_region)))

    def get_payment_checkbox(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.payment_checkbox)))

    def get_next_button_payment(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.next_button_payment)))

    def get_delivery_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.delivery_button)))

    def get_next_button_delivery(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.next_button_delivery)))

    def get_field_client_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.field_client_name)))

    def get_field_email(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.field_email)))

    def get_field_phone_number(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.field_phone_number)))

    def get_next_button_client_info(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.next_button_client_info)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_back_main_page_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.back_main_page_button)))

    def get_main_word_main_page(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.main_word_main_page)))

    def get_cart_button_main_page(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart_button_main_page)))

    def get_clear_basket_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.clear_basket_button)))

    # Actions

    def click_radion_button(self):
        self.get_radion_button().click()
        print("Click radio button")

    def click_address_field(self):
        self.get_address_field().clear()
        self.get_address_field().send_keys('Санкт-Петербург')
        self.get_address_field().send_keys(Keys.ARROW_DOWN)
        self.get_address_field().send_keys(Keys.BACKSPACE)
        print("Click address field")

    def click_address_field_help(self):
        self.get_address_field_help().click()
        print("Click address field help")


    def click_next_button_region(self):
        self.get_next_button_region().click()
        print("Click next button region")

    def click_payment_checkbox(self):
        self.get_payment_checkbox().click()
        print("Click payment checkbox")

    def click_next_button_payment(self):
        self.get_next_button_payment().click()
        print("Click next button payment")

    def click_delivery_button(self):
        self.get_delivery_button().click()
        print("Click delivery button")

    def click_next_button_delivery(self):
        self.get_next_button_delivery().click()
        print("Click next button delivery")

    def click_field_client_name(self):
        self.get_field_client_name().clear()
        self.get_field_client_name().send_keys("Годенко Владислав")
        print("Click field client name")

    def click_field_email(self):
        self.get_field_email().clear()
        self.get_field_email().send_keys("qa.godenko@gmail.com")
        print("Click field email")

    def click_field_phone_number(self):
        self.get_field_phone_number().clear()
        self.get_field_phone_number().send_keys("9997766555")
        print("Click field phone number")

    def click_next_button_client_info(self):
        self.get_next_button_client_info().click()
        print("Click next button client info")

    def click_back_main_page_button(self):
        self.get_back_main_page_button().click()
        print("Click back main page button")

    def click_cart_button_main_page(self):
        self.get_cart_button_main_page().click()
        print("Click cart button main page")

    def click_clear_basket_button(self):
        self.get_clear_basket_button().click()
        print("Click clear basket button")

    # Methods


    def placing_order(self):
        self.click_radion_button()
        time.sleep(2)
        self.click_address_field()
        time.sleep(2)
        self.click_address_field_help()
        time.sleep(2)
        self.click_next_button_region()
        time.sleep(2)
        self.click_payment_checkbox()
        time.sleep(2)
        self.click_next_button_payment()
        time.sleep(2)
        self.click_delivery_button()
        time.sleep(2)
        self.click_next_button_delivery()
        time.sleep(2)
        self.click_field_client_name()
        time.sleep(2)
        self.click_field_email()
        time.sleep(2)
        self.click_field_phone_number()
        time.sleep(2)
        self.click_next_button_client_info()
        time.sleep(2)
        self.assert_word(self.get_name_product(), 'Смартфон ASUS Zenfone 11 Ultra 16/512GB Blue (Синий)')
        time.sleep(2)
        self.assert_word(self.get_price_product(), '95 490')
        time.sleep(2)
        self.click_back_main_page_button()
        time.sleep(2)
        self.assert_word(self.get_main_word_main_page(), 'Интернет-магазин техники и электроники Телемаркет24')
        time.sleep(2)
        self.click_cart_button_main_page()
        time.sleep(2)
        self.click_clear_basket_button()
        time.sleep(2)



