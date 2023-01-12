from selenium.webdriver.common.by import By
from Test.BaseTest.base import *


class Test_Valid_ForgetPassword(BaseTest):
    def test_Facebook_ForgetPassword_Functionality_with_Valid_Email(self):
        driver = super().initial()
        driver.find_element(By.XPATH, ForgetPassword_Path).click()  # Click Forget Password link
        findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount_Path).text  # Display Find Your Account page
        assert "Find Your Account" == findYourAccount_Page
        identifyEmail = driver.find_element(By.XPATH, IdentifyEmail_ElementPath)  # Enter Email address
        identifyEmail.clear()
        identifyEmail.send_keys(ForgetPassword_Valid_Email)
        driver.find_element(By.XPATH, Email_Search_Button).click()  # Click Search button
        IdentifyYourAccount_Page = driver.find_element(By.XPATH,
                                                       IdentifyYourAccount_ElementPath).text  # Display Identify your account Page
        assert "Identify your account" == IdentifyYourAccount_Page
        driver.find_element(By.XPATH, MyAccount_Button).click()  # Click This is my account button
        ResetYourPassword_Page = driver.find_element(By.XPATH,
                                                     ResetYourPasswordPage_ElementPath).text  # Display Reset Your Password Page
        assert 'Reset Your Password' == ResetYourPassword_Page
        driver.find_element(By.XPATH, SendCodeViaEmailButton_ElementPath).click()  # Select "Send code via email" button
        driver.find_element(By.XPATH, ResetPassword_continueButton).click()  # Click on Continue Button
        securityCodePage = driver.find_element(By.XPATH,
                                               EnterSecurityCodePage_ElementPath).text  # Display Enter security code page
        assert "Enter security code" == securityCodePage
        recovery_code_entry = driver.find_element(By.XPATH, RecoveryCodeEntry_ElementPath)  # Recovery Code Entry
        recovery_code_entry.clear()
        recovery_code_entry.send_keys("740515")
        driver.find_element(By.XPATH, ResetPassword_continueButton).click()  # Click on Continue Button
        newPassword_Page = driver.find_element(By.XPATH, NewPasswordPage_ElementPath).text  # Display New Password page
        assert "Choose a new password" == newPassword_Page
        newpassword_entry = driver.find_element(By.NAME, "password_new")
        newpassword_entry.send_keys("password1234")
        driver.find_element(By.XPATH, NewPassword_ContinueButton).click()  # Click Continue Button
        Facebook_Home = driver.current_url  # Display Facebook User Home page
        assert Facebook_Home == Facebook_Web_Address
        super().tear_down()
