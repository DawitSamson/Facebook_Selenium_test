# This Locator is the Xpath Url for Facebook website which help us on testing functionality code display Clearly

# Main Facebook address
Facebook_Web_Address = "https://www.facebook.com/"

# Facebook information
Login_Valid_Email = "davidisking@gmail.com"
Login_Valid_Password = "password"
Login_Invalid_Email = "asffsafuts"
Login_Invalid_Password = "32454hfr6"


# Facebook Login Paths.
Input_Login_Email_Address_Path = "//input[@id='email']"
input_login_Password_path = "//input[@id='pass']"
Login_Button = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]"
# login error
Login_Invalid_EmailAndPassword_ErrorMessage = "//div[contains(text(),'Invalid username or password')]"
Login_ValidEmail_And_InvalidPassword_ErrorMessage = "//div[contains(text(),'Invalid username or password')]"
Login_InvalidEmail_And_ValidPassword_ErrorMessage = "//div[contains(text(),'Invalid username or password')]"
Login_Blank_EmailAndPassword_ErrorMessage = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/a[1]"

# Facebook ForgetPassword Paths
ForgetPassword_Path = "//a[contains(text(),'Forgotten password?')]"
FindYourAccount_Path = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
IdentifyEmail_ElementPath = "//input[@id='identify_email']"
ForgetPassword_Valid_Email = "youremail@***.com"
ForgetPassword_Invalid_Email = "d@.com"
Email_Search_Button = "//button[@id='did_submit']"
IdentifyYourAccount_ElementPath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
MyAccount_Button = "//a[contains(text(),'This is my account')]"
ResetYourPasswordPage_ElementPath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
SendCodeViaEmailButton_ElementPath = "//input[@id='send_email']"
ResetPassword_continueButton = "//button[contains(text(),'Continue')]"
EnterSecurityCodePage_ElementPath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
RecoveryCodeEntry_ElementPath = "//input[@id='recovery_code_entry']"
NewPasswordPage_ElementPath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
NewPassword_ContinueButton = "//button[@id='btn_continue']"
NoSearchResults_ErrorMessage = "//div[contains(text(),'No search results')]"
PleaseFillInAtLeastOneField_ErrorMessage = "//div[contains(text(),'Please fill in at least one field')]"

# Facebook SignUp Paths
CreateNewAccount_Path = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[5]/a[1]"
SignUp_PagePath = "//div[contains(text(),'Sign Up')]"
FirstName_ElementPath = "firstname"
LastName_ElementPath = "lastname"
EmailInput_ElementPath = "reg_email__"
EmailReEnter_ElementPath = "reg_email_confirmation__"
Password_ElementPath = "reg_passwd__"
BirthDay_ElementPath = "//select[@id='day']"
BirthMonth_ElementPath = "//select[@id='month']"
BirthYear_ElementPath = "//select[@id='year']"
GenderSelect_ElementPath = "/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[7]/span[1]/span[2]/input[1]"
SignUp_ButtonPath = "/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[11]/button[1]"
Email_ConformationPath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
Continue_ButtonPath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/button[1]"
Ok_ButtonPath = "//a[contains(text(),'OK')]"
Error_nullAll = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]"
Error_InvalidEmail = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]"
Error_nullGender = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]"
Error_nullFirstName = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]"
Error_nullLastName = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]"
Error_Birthday = "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]"
