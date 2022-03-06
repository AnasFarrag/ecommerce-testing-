from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    text_username_id = "Email"
    text_password_id = "Password"
    login_button_xpath = "//button[contains(text(),'Log in')]"
    logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        driver = self.driver
        driver.find_element(By.ID, self.text_username_id).clear()
        driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def enter_password(self, password):
        driver = self.driver
        driver.find_element(By.ID, self.text_password_id).send_keys(Keys.DELETE)
        #driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def click_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, self.logout_link_text).click()

