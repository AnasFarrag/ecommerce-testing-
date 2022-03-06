import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage

global driver
driver = webdriver.Chrome(ChromeDriverManager().install())


class TestLogin001:
    base_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin@yourstore.com"
    login_page_title = "Your store. Login222"
    home_page_title = "Dashboard / nopCommerce administration22"

    @pytest.fixture()
    def test_setup(self):
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()

    def test_login_01(self):
        driver.get(self.base_url)
        assert driver.title == self.login_page_title

    def test_login_02(self, test_setup):
        driver.get(self.base_url)
        self.lp = LoginPage(driver)
        self.lp.enter_username(self.username)
        time.sleep(3)
        self.lp.enter_password(self.password)
        time.sleep(4)
        self.lp.click_login()
        time.sleep(4)
        if driver.title == self.home_page_title:
            assert True
        else:
            driver.save_screenshot('.\\Screenshots\\' + "test_homapagetitle.png")
            assert False
