from selenium.webdriver.common.by import By
import time

class SearchCustomer():
    # Add customer Page
    txtEmail_id = "SearchEmail" #using id when available is most recommended, because id's are unique
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"
    openSearch_xpath = "//div[@class='row search-row ']"

    # tblSearchResults_xpath="//table[@id='customers-grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def openSearch(self):
        try:
            self.driver.find_element(By.XPATH, self.openSearch_xpath).click()
            time.sleep(3)
        except Exception:
            pass

    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1, self.getNoOfRows()+1): #loop through the rows available
          table = self.driver.find_element(By.XPATH, self.table_xpath)
          emailid = table.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1, self.getNoOfRows()+1):
          table=self.driver.find_element(By.XPATH, self.table_xpath)
          name = table.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag


