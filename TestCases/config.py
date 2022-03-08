import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def setup():
    # if browser == "chrome":
    #     print("Launching Chrome Browser")
    #     return webdriver.Chrome(ChromeDriverManager().install())
    # elif browser == "firefox":
    #     print("Launching Firefox Browser")
    return webdriver.Chrome(ChromeDriverManager().install())
    # return webdriver.Firefox(GeckoDriverManager().install())

#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")


## Writting Html Report
def pytest_configure(config):
    config._metadata['Project Name'] = "nop commerce"
    config._metadata['Module Name'] = "customers"
    config._metadata['Tester'] = "Anas Farrag"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
