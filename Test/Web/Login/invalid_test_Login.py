from selenium.webdriver.common.by import By
from Test.BaseTest.base import *


class Test_Invalid_Login(BaseTest):
    def test_Facebook_Login_Functionality_with_Invalid_Email_and_Password(self):
        driver = super().initial()
        email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
        email.clear()
        email.send_keys(Login_Invalid_Email)
        password = driver.find_element(By.XPATH, input_login_Password_path)
        password.clear()
        password.send_keys(Login_Invalid_Password)
        driver.find_element(By.XPATH, Login_Button).click()  # Click login button.
        Error_message = driver.find_element(By.XPATH, Login_Invalid_EmailAndPassword_ErrorMessage).text
        assert 'Invalid username or password' == Error_message
        super().tear_down()

    def test_Facebook_Login_Functionality_with_Valid_Email_and_Invalid_Password(self):
        driver = super().initial()
        email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
        email.clear()
        email.send_keys(Login_Valid_Email)
        password = driver.find_element(By.XPATH, input_login_Password_path)
        password.clear()
        password.send_keys(Login_Invalid_Password)
        driver.find_element(By.XPATH, Login_Button).click()  # Click login button
        Error_message = driver.find_element(By.XPATH, Login_ValidEmail_And_InvalidPassword_ErrorMessage).text
        assert 'Invalid username or password' == Error_message
        super().tear_down()

    def test_Facebook_Login_Functionality_with_Invalid_Email_and_Valid_Password(self):
        driver = super().initial()
        email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
        email.clear()
        email.send_keys(Login_Invalid_Email)
        password = driver.find_element(By.XPATH, input_login_Password_path)
        password.clear()
        password.send_keys(Login_Valid_Password)
        driver.find_element(By.XPATH, Login_Button).click()  # Click login button
        Error_message = driver.find_element(By.XPATH, Login_InvalidEmail_And_ValidPassword_ErrorMessage).text
        assert 'Invalid username or password' == Error_message
        super().tear_down()

    def test_Facebook_Login_Functionality_with_Blank_Email_and_Password(self):
        driver = super().initial()
        driver.find_element(By.XPATH, Login_Button).click()  # Click login button
        Error_message = driver.find_element(By.XPATH, Login_Blank_EmailAndPassword_ErrorMessage).text
        assert "Find your account and log in." == Error_message
        super().tear_down()

    def test_Facebook_Login_Functionality_with_Valid_Email_and_Blank_Password(self):
        driver = super().initial()
        email = driver.find_element(By.XPATH, Input_Login_Email_Address_Path)
        email.clear()
        email.send_keys(Login_Valid_Email)
        driver.find_element(By.XPATH, Login_Button).click()   # Click login button
        Error_message = driver.find_element(By.XPATH, Login_Blank_EmailAndPassword_ErrorMessage).text
        assert 'Invalid username or password' == Error_message
        super().tear_down()
