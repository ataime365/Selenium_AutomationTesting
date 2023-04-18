from selenium import webdriver
import pytest
import logging

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser=='edge':
        driver = webdriver.Edge() #Microsoft Edge Internet explorer as default browser
        print("Launching Edge browser")
    return driver

def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the Browser value to setup method
    return request.config.getoption("--browser")



############## PyTest HTML Report ############

# It is the hook for adding Environment info to the HTMl Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Benson'
    
    # This helps us register the grouping markers we are using to run tests
    config.addinivalue_line("markers", "sanity: mark test as a sanity test")
    config.addinivalue_line("markers", "regression: mark test as a regression test")
    config.addinivalue_line("markers", "performance: mark test as a performance test")


# This is the hook to delete/modify the default Environment info in the HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
