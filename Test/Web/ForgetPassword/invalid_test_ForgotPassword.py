from Test.BaseTest.base import *


class Test_Valid_ForgetPassword(BaseTest):

    def test_Facebook_ForgetPassword_Functionality_with_Invalid_Email(self):
        driver = super()
        driver.initial()                                            # Initial Webf address
        driver.click(ForgetPassword_Path)                           # Click Forget Password link
        findYourAccount_Page = driver.text(FindYourAccount_Path)    # Finf "Find Your Account page" text
        assert "Find Your Account" == findYourAccount_Page           # Display Find Your Account page
        driver.send_key(IdentifyEmail_ElementPath,ForgetPassword_Invalid_Email)  # Enter Email address
        driver.click(Email_Search_Button)                                         # Click Search button
        errorMessage = driver.text(NoSearchResults_ErrorMessage)  # Display Error Message
        assert "No search results" == errorMessage
        driver.tear_down()

    def test_Facebook_ForgetPassword_Functionality_with_Null_Email(self):
        driver = super().initial()
        driver.find_element(By.XPATH, ForgetPassword_Path).click()       # Click Forget Password link
        findYourAccount_Page = driver.find_element(By.XPATH,FindYourAccount_Path).text  # Display Find Your Account page.
        assert "Find Your Account" == findYourAccount_Page
        driver.find_element(By.XPATH,Email_Search_Button).click()  # Click Search button
        IdentifyYourAccount_Page = driver.find_element(By.XPATH,PleaseFillInAtLeastOneField_ErrorMessage).text  # Display Error Message
        assert "Please fill in at least one field" == IdentifyYourAccount_Page
        super().tear_down()
