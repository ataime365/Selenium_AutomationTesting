from selenium.webdriver.common.by import By

class LoginPage:
    # Writing the locators
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout" 


    def __init__(self, driver):
        """driver comes from the actual test case"""
        self.driver = driver


    def setUserName(self, username):
        """username comes from the actual test case, These are action methods"""
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        """password comes from the actual test case, These are action methods"""
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        """Implementing action method for this element"""
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()







