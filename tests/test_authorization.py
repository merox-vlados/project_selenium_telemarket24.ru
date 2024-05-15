import time

from pages.login_page import LoginPage
from utilities.driver import Driver


def test_authorization(set_up):

    """Test user authorization"""

    driver = Driver().chrome_driver()

    lp = LoginPage(driver) # login_page
    lp.authorization()

