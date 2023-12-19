from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Data import data
from Locators import locators
from time import sleep


class Test_2:
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
   
    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebApp_Data().url)
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().username_input_box).send_keys(data.WebApp_Data().username)
            sleep(4)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().password_input_box).send_keys(data.WebApp_Data().password)
            sleep(4)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().submit_button).click()
            sleep(4)
            
            

        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.quit()


Test_2().login()
print('Please enter a valid password')

