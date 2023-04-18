import pytest
# from selenium import webdriver #For development purpose
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage #We have to login to test this feature
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

import string, random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    # def __init__(self): #Just for development purpose only
    #     self.driver = webdriver.Chrome() #Just for development purpose

    @pytest.mark.sanity
    def test_addCustomer(self, setup): #setup is the name of the fixture in conftest.py
        self.logger.info("************** Test_003_AddCustomer ********************")
        self.driver = setup #uncomment this when done
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login successful ***********")

        self.logger.info("****** Starting Add Customer Test ****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerSubMenu()

        self.addcust.ClickOnAddnew()

        self.logger.info("************** Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Ataime")
        self.addcust.setLastName("Okodi")
        self.addcust.setDob("7/05/1980") #Format: D/MM/ YY
        self.addcust.setCompanyName("BenQA")
        self.addcust.setAdminContent("This is for testing..........")
        self.addcust.clickOnSave()

        self.logger.info("************ Saving customer info ************")

        self.logger.info("************ Add customer validation started ************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test passed *********")
        else:
            self.driver.save_screenshot(".\\Screnshots\\" + "test_addCustomer_scr.png") #Screenshot
            self.logger.error("********** Add customer Test Failed *********")
            assert False

        self.driver.close()
        self.logger.info("******** Ending Test_003_AddCustomer Test *********")




def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    """chars generates a long string, random.choice chooses letters or words in the string
    the list conprehestion creates a list using each character, join converts it to a string"""
    return ''.join(random.choice(chars) for x in range(size))


