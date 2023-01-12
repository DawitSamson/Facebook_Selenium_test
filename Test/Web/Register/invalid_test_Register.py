from selenium.webdriver.common.by import By
from Test.BaseTest.base import *


class Test_Invalid_Register(BaseTest):
    def test_Facebook_Registering_with_Invalid_information_Using_Null_on_all_fields(self):
        driver = super().initial()
        driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
        error_Message = driver.find_element(By.XPATH,Error_nullAll).text  # Display Error Message
        assert '' == error_Message
        super().tear_down()

    def test_Facebook_Registering_with_Invalid_Email(self):
        driver = super().initial()
        driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
        signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
        assert 'Sign Up' == signUp_Page
        firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
        firstName_box.send_keys("david")  # entering first name
        surname_box = driver.find_element(By.NAME,LastName_ElementPath)
        surname_box.send_keys("belay")  # entering Last name
        registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
        registerEmail_box.send_keys("david@yahoo.com")  # entering email address
        registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
        registerReEnterEmail_box.send_keys("00000@yahoo.com")  # entering Re-enter email address
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
        error_Message = driver.find_element(By.XPATH,Error_InvalidEmail).text  # Display Error Message
        assert '' == error_Message
        super().tear_down()

    def test_Facebook_Registering_With_Null_Gender(self):
        driver = super().initial()
        driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
        signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
        assert 'Sign Up' == signUp_Page
        firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
        firstName_box.send_keys("david")  # entering first name
        surname_box = driver.find_element(By.NAME,LastName_ElementPath)
        surname_box.send_keys("belay")  # entering Last name
        registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
        registerEmail_box.send_keys("david@yahoo.com")  # entering email address
        registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
        registerReEnterEmail_box.send_keys("david@yahoo.com")  # entering Re-enter email address
        registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
        registerPassword_box.send_keys("password1234")  # entering password
        birthDay_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
        birthDay_box.send_keys("1")  # entering Birth Day
        birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
        birthMonth_box.send_keys("jul")  # enter Birth Month
        birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
        birthYear_box.send_keys("2000")  # entering Birth Year
        driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
        error_Message = driver.find_element(By.XPATH,Error_nullGender).text  # Display Error Message
        assert '' == error_Message
        super().tear_down()

    def test_Facebook_Registering_with_Null_FirstName(self):
        driver = super().initial()
        driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
        signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
        assert 'Sign Up' == signUp_Page
        surname_box = driver.find_element(By.NAME, LastName_ElementPath)
        surname_box.send_keys("belay")  # entering Last name
        registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
        registerEmail_box.send_keys("david@yahoo.com")  # entering email address
        registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
        registerReEnterEmail_box.send_keys("david@yahoo.com")  # entering Re-enter email address
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
        error_Message = driver.find_element(By.XPATH,Error_nullFirstName).text  # Display Error Message
        assert '' == error_Message
        super().tear_down()

    def test_Facebook_Registering_with_Null_LastName(self):
        driver = super().initial()
        driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
        signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
        assert 'Sign Up' == signUp_Page
        firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
        firstName_box.send_keys("david")  # entering first name
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
        error_Message = driver.find_element(By.XPATH,Error_nullLastName).text  # Display Email conformation page
        assert '' == error_Message
        super().tear_down()

    def test_Facebook_Registering_with_Null_Birthday(self):
        driver = super().initial()
        driver.find_element(By.XPATH, CreateNewAccount_Path).click()  # Click Create New Account button
        signUp_Page = driver.find_element(By.XPATH,SignUp_PagePath).text  # Display Signup page
        assert 'Sign Up' == signUp_Page
        firstName_box = driver.find_element(By.NAME,FirstName_ElementPath)
        firstName_box.send_keys("david")  # entering first name
        surname_box = driver.find_element(By.NAME, LastName_ElementPath)
        surname_box.send_keys("belay")  # entering Last name
        registerEmail_box = driver.find_element(By.NAME,EmailInput_ElementPath)
        registerEmail_box.send_keys("youremail@****.com")  # entering email address
        registerReEnterEmail_box = driver.find_element(By.NAME,EmailReEnter_ElementPath)
        registerReEnterEmail_box.send_keys("youremail@****.com")  # entering Re-enter email address
        registerPassword_box = driver.find_element(By.NAME,Password_ElementPath)
        registerPassword_box.send_keys("password1234")  # entering password
        birthMonth_box = driver.find_element(By.XPATH,BirthMonth_ElementPath)
        birthMonth_box.send_keys("jul")  # entering Birth Month
        birthYear_box = driver.find_element(By.XPATH,BirthDay_ElementPath)
        birthYear_box.send_keys("2000")  # entering Birth Year
        driver.find_element(By.XPATH,GenderSelect_ElementPath).click()  # Select Gender
        driver.find_element(By.XPATH,SignUp_ButtonPath).click()  # Click Sign Up Button
        error_Message = driver.find_element(By.XPATH,Error_Birthday).text  # Display Email conformation page
        assert '' == error_Message
        super().tear_down()

