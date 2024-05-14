from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Driver:

    def __init__(self):
        pass

    def chrome_driver(self):

        path_chromedriver_d = 'D:/QA_Engineer/PyChar/resource/chromedriver.exe'
        path_chromedriver_c = 'C:/Users/merox/Desktop/QA/resource/chromedriver.exe'

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("detach", True)
        options.page_load_strategy = 'eager'
        chrome_service = Service(path_chromedriver_c)

        capabilities = options.to_capabilities()
        capabilities['acceptInsecureCerts'] = True


        driver = webdriver.Chrome(options=options, service=chrome_service)

        return driver