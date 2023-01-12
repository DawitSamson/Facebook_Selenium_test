from selenium import webdriver
from Locators.Locators_Facebook import *
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BaseTest:
    driver = webdriver.Chrome()  # the web driver which we are going to use is Chrome

    def initial(self):
        self.driver.get(Facebook_Web_Address)  # Get used to get the URL in the driver
        self.driver.maximize_window()  # Maximize web window
        sleep(1)  # It is the page load timeout sec
        Facebook_HomePage = self.driver.title  # find Facebook HomePage
        assert 'Facebook – log in or sign up' == Facebook_HomePage  # Check if Facebook HomePage displayed
        return self.driver

    def tear_down(self):
        self.driver.close()

    def click(self, path_locators):
        return self.driver.find_element(By.XPATH, path_locators).click()

    def text(self, path_locators):
        return self.driver.find_element(By.XPATH, path_locators).text

    def send_key(self, path_locators, text):
        return self.driver.find_element(By.XPATH, path_locators).send_keys(text)


def is_element_exist(text, webElement):
    try:
        return webElement.find_element(By.CLASS_NAME, text).text
    except NoSuchElementException:
        return ''




