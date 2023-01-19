from selenium.webdriver.common.by import By
from Test.BaseTest.base import *


class Test_Valid_Register(BaseTest):
    def test_Facebook_Validate_Registering_with_Valid_information_by_providing_all_the_fields(self):
        driver = super().initial()
        driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
        signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
        assert 'Sign Up' == signUp_Page
        firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
        firstName_box.send_keys("david")  # entering first name
        surname_box = driver.find_element(By.NAME,LastName_ElementPath)
        surname_box.send_keys("belay")  # entering Last name
        registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
        registerEmail_box.send_keys("youremail@****.com")  # entering email address
        registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
        registerReEnterEmail_box.send_keys("youremail@****.com")  # entering Re-enter email address
        registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
        registerPassword_box.send_keys("password1234")  # entering password
        birthDay_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
        birthDay_box.send_keys("1")  # entering Birth Day
        birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
        birthMonth_box.send_keys("jul")  # entering Birth Month
        birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
        birthYear_box.send_keys("2000")  # entering Birth Year
        driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
        driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
        email_conformation_Page = driver.find_element(By.XPATH,Email_ConformationPath).text  # Display Email conformation page
        assert 'Enter the code from your email' == email_conformation_Page
        enterConformationNumber = driver.find_element(By.NAME, "code")
        enterConformationNumber.send_keys("54321")  # entering conformation number
        driver.find_element(By.XPATH,Continue_ButtonPath).click()  # Click Continue Button
        accountConform_page = driver.find_element(By.NAME,"Account Confirmed").text  # Display Account conformation page
        assert 'Account Confirmed' == accountConform_page
        driver.find_element(By.XPATH,Ok_ButtonPath).click()  # Click Ok button
        Facebook_Home = driver.current_url  # Display Facebook User Home page
        assert Facebook_Home == Facebook_Web_Address
        super().tear_down()
