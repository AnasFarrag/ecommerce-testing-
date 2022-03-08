import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser):
    if browser == "chrome":
        print("Launching Chrome Browser")
        return webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        print("Launching Firefox Browser")
        return webdriver.Firefox(GeckoDriverManager().install())


## Writting Html Report
def pytest_configure(config):
    config._metadata['Project Name'] = "nop commerce"
    config._metadata['Module Name'] = "customers"
    config._metadata['Tester'] = "Anas Farrag"


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
