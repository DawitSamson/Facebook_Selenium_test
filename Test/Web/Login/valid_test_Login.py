from selenium.webdriver.common.by import By
from Test.BaseTest.base import *


class Test_Valid_Login(BaseTest):
    def test_Facebook_Login_Functionality_with_Valid_Email_and_Password(self):
        driver = super().initial()
        email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
        email.clear()
        email.send_keys(Login_Valid_Email)          # enter valid email
        password = driver.find_element(By.XPATH, input_login_Password_path)
        password.clear()
        password.send_keys(Login_Valid_Password)             # enter valid password
        driver.find_element(By.XPATH, Login_Button).click()  # Click login button
        Facebook_Home = driver.current_url
        assert Facebook_Home == Facebook_Web_Address
        super().tear_down()
