from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.AccountPage import AccountPage
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_tearDown_code")
class TestLogin:
    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"paran{time_stamp}@gmail.com"


    def test_01_login_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.log_in_to_the_application("paranchoudhury05@gmail.com","123456")

        # login_page.enter_valid_email_address("paranchoudhury05@gmail.com")
        # login_page.enter_valid_password("123456")
        # account_page = login_page.click_on_login_button()
        # ✅ Wait for the "Edit your account information" link
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Edit your account information"))

        )

        assert account_page.account_page_link_text_verify()



    def test_02_login_with_invalid_email_and_valid_password(self):

        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.log_in_to_the_application(self.generate_email_with_time_stamp(), "123456")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        # ✅ Wait for the alert to appear
        alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger"))
        )

        assert login_page.login_page_warning_message_css_selector_retrieve().__eq__(expected_warning_message)




    def test_03_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page =  home_page.navigate_to_login_page()
        login_page.log_in_to_the_application("paranchoudhury05@gmail.com","wrongpassword123")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."

        # ✅ Wait for alert
        alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger"))
        )
        assert login_page.login_page_warning_message_css_selector_retrieve().__eq__(expected_warning_message)



    def test_04_login_without_any_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.log_in_to_the_application("","")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."

        # ✅ Wait for alert
        alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger"))
        )
        assert login_page.login_page_warning_message_css_selector_retrieve().__eq__(expected_warning_message)
