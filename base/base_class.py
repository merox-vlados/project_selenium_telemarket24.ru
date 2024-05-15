import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert main word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Good value word ({value_word} == {result})")

    """Method take screenshot"""

    def get_screenshot(self):
        path_screen_c = 'C:\\Users\\merox\\Desktop\\QA\\project_selenium_telemarket24.ru\\screen\\'
        path_screen_d = 'D:\\QA_Engineer\\PyChar\\project_selenium_telemarket24.ru\\screen\\'

        now_date = datetime.datetime.now().strftime("%d.%m.%Y_%H-%M-%S")
        name_screenshot = "screenshot_" + now_date + '.png'
        self.driver.save_screenshot(path_screen_d + name_screenshot)

    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"Good value url : {get_url} == {result}")
