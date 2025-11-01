# from adodbapi.examples.xls_read import driver
from selenium.webdriver.common.by import By

from PageObjects.AccountPage import AccountPage


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    email_address_by_id ="input-email"
    Password_by_id ="input-password"
    login_button_xpath ="//input[@value='Login']"
    login_page_warning_message_Css_selector ="div.alert.alert-danger"

    def enter_valid_email_address(self,email_address_text):
        self.driver.find_element(By.ID,self.email_address_by_id).click()
        self.driver.find_element(By.ID,self.email_address_by_id).clear()
        self.driver.find_element(By.ID,self.email_address_by_id).send_keys(email_address_text)
    def enter_valid_password(self,password_text):
        self.driver.find_element(By.ID,self.Password_by_id).click()
        self.driver.find_element(By.ID,self.Password_by_id).clear()
        self.driver.find_element(By.ID,self.Password_by_id).send_keys(password_text)
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        return AccountPage(self.driver)
    def login_page_warning_message_css_selector_retrieve(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.login_page_warning_message_Css_selector).text

    def log_in_to_the_application(self, email_address_text,password_text):
        self.enter_valid_email_address(email_address_text)
        self.enter_valid_password(password_text)
        return self.click_on_login_button()
