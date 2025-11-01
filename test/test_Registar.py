
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.AccountSuccessPage import AccountSuccess
from PageObjects.HomePage import HomePage
from PageObjects.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_tearDown_code")
class TestRegister:


    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f"paran{time_stamp}@gmail.com"



    def test_01_Registar_with_Mandatory_fields(self):

        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success = register_page.register_with_mandatory_fields("Paran","Choudhury",self.generate_email_with_time_stamp(),"123456","123456","123456","no","select")



        expected_message="Your Account Has Been Created!"



        assert account_success.accountSuccess_status_verify().__eq__(expected_message)



    def test_02_Register_with_all_fields_and_Yes_subscribe_button(self):

        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success = register_page.register_with_mandatory_fields("Paran","Choudhury",self.generate_email_with_time_stamp(),"123456","123456","123456","yes","select")



        expected_message = "Your Account Has Been Created!"


        assert account_success.accountSuccess_status_verify().__eq__(expected_message)




    def test_03_Register_with_Duplicate_email_address(self):


        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_with_mandatory_fields("Paran", "Choudhury",
                                                                       "paran25021998@gmail.com", "123456",
                                                                       "123456", "123456", "yes", "select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"

        assert register_page.Validate_Duplicate_email_entry_warning_message().__eq__(expected_warning_message)



    def test_04_Register_without_any_fields(self):



        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_with_mandatory_fields(first_name="",last_name="",email_text=
                                                     "",telephone_number="",
                                                     password_text="",confirm_text="",yes_or_no="",privacy_policy="")
        register_page.verify_all_warning_message("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")

       











    '''
        expected_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]").text.__contains__(expected_warning_message)
        expected2 ="First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected2)
        expected3 ="Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(expected3)
        expected4 ="E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(expected4)
        expected5 ="Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(expected5)
        expected6= "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(expected6)

    '''







