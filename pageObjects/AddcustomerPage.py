import time
from selenium.webdriver.common.by import By
from selenium import webdriver #Just for development purpose
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    lnkCustomers_submenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(), 'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"

    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitemForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    lstitemGuests_xpath = "//li[contains(text(), 'Guests')]"
    lstitemRegistered_xpath = "//li[contains(text(), 'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(), 'Vendors')]"

    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    chkbTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        """driver will come from the actual test case"""
        self.driver = driver
        # self.driver = webdriver.Chrome() #Just for development purpose

    def clickOnCustomerMenu(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerSubMenu(self):
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, self.lnkCustomers_submenu_xpath).click()

    def ClickOnAddnew(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)


    def setCustomerRoles(self, role):
        """To set multiple roles, we have to call this function multiple times"""
        # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.txtCustomerRoles_xpath)))
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        # Only pick one Role
        if role == 'Registered':
            # Saving it for clicking later
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            #Delete Registered by clicking x , span...... Then add Guests xpath
            self.driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        # elif role=='Registered':
        #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            #Use Guests as our default
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem) #Using Javascrip to click

    def setManagerOfVendor(self,value):
        """Select is used when the given element is a select tag"""
        drp=Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)
        time.sleep(1)

    def setGender(self, gender):
        if gender=='Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            #Make this our Default
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()



    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, compname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(compname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
   














