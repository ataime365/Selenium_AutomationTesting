import pytest  #we can also use behave, rewrite this test in behave and features
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".\\TestData\\LoginData.xlsx"  #Dynamic data

    logger = LogGen.loggen()
            
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********* Test_002_DDT_Login ***************")
        self.logger.info("************** Verifying Login DDT test ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows:", self.rows)

        lst_status = []
        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3) #3 column number
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration" #exp_title means expected_title
            if act_title == exp_title: #login test
                if self.exp == "Pass": #Excel sheet text #This is our expected outcome #Database test
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout() #The driver is already incorporated in the lp page
                    lst_status.append("Pass")
                elif self.exp == "Fail": #Data test, this details shouldnt have access but it did, so it is a fail, bug
                    self.logger.info("*** failed ***")
                    self.lp.clickLogout() #The driver is already incorporated in the lp page
                    lst_status.append("Fail")
            elif act_title != exp_title: #login test #didnt login
                # parsing Invalid data 
                # The expected here is "Fail", if it is "Pass" then it fails
                if self.exp == "Pass": #For the Invalid data, This field shouldnt be "Pass" in the excel file, if it is, then the Excel sheet has a bug
                    self.logger.info("*** failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail": #Data test, this details shouldnt have access but it did, so it is a fail, bug
                    # Parsing invalid data should give us a "Fail" 
                    self.logger.info("*** passed ***")
                    lst_status.append("Pass")

        # Final status #The real test output
        if "Fail" not in lst_status:
            self.logger.info("******* Login DDT test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed *******")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("******* Completed TC_LoginDDT_002 **********")





# pytest -s -v -n=2 --html=Reports\report.html testCases\test_login.py --browser chrome