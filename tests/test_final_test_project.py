import allure

from pages.cart_page import CartPage
from pages.ordering_page import OrderingPage
from pages.smartphones_catalog_page import SmartphonesCatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from utilities.driver import Driver


@allure.description("Test final test project")
def test_final_test_project(set_up):

    """Test business way from authorization to ordering"""

    driver = Driver().chrome_driver()

    lp = LoginPage(driver)  # login_page
    lp.authorization()

    mp = MainPage(driver)  # main_page
    mp.choosing_category()

    scp = SmartphonesCatalogPage(driver) # smartphones_catalog_page
    scp.select_product_1()

    pp = ProductPage(driver) # product_page
    pp.change_parameters_and_select_product()

    cp = CartPage(driver) # cart_page
    cp.check_order()

    op = OrderingPage(driver) # ordering_page
    op.placing_order()