from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.AccountSuccessPage import AccountSuccess


class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    first_name_field_ID = "input-firstname"
    last_name_field_ID = "input-lastname"
    email_ID = "input-email"
    telephone = "input-telephone"
    password_ID ="input-password"
    confirm_password ="input-confirm"
    agree_check_box_field ="//input[@name='agree']"
    continue_button ="//input[@value='Continue']"
    Subscribe_check_yes_XPATH ="//input[@name='newsletter'][@value='1']"
    Duplicate_email_entry_CSS_Selector ="div.alert.alert-danger"
    Privacy_policy_warning_message_xpath ="//div[contains(@class, 'alert-danger')]"
    Expected_first_name_warning_message_xpath ="//input[@id='input-firstname']/following-sibling::div"
    Expected_last_name_warning_message_xpath ="//input[@id='input-lastname']/following-sibling::div"
    Expected_email_warning_message ="//input[@id='input-email']/following-sibling::div"
    Expected_telephone_warning_message ="//input[@id='input-telephone']/following-sibling::div"
    Expected_password_warning_message ="//input[@id='input-password']/following-sibling::div"


    def enter_first_name_field_id(self,first_name):
        self.driver.find_element(By.ID,self.first_name_field_ID).click()
        self.driver.find_element(By.ID,self.first_name_field_ID).clear()
        self.driver.find_element(By.ID,self.first_name_field_ID).send_keys(first_name)

    def enter_last_name_field_ID(self,last_name):
        self.driver.find_element(By.ID,self.last_name_field_ID).click()
        self.driver.find_element(By.ID,self.last_name_field_ID).clear()
        self.driver.find_element(By.ID,self.last_name_field_ID).send_keys(last_name)

    def enter_email_field_ID(self,email_text):
        self.driver.find_element(By.ID,self.email_ID).send_keys(email_text)

    def enter_telephone_number_ID(self,telephone_number):
        self.driver.find_element(By.ID,self.telephone).click()
        self.driver.find_element(By.ID,self.telephone).clear()
        self.driver.find_element(By.ID,self.telephone).send_keys(telephone_number)

    def enter_password_ID(self,password_text):
        self.driver.find_element(By.ID,self.password_ID).click()
        self.driver.find_element(By.ID,self.password_ID).clear()
        self.driver.find_element(By.ID,self.password_ID).send_keys(password_text)

    def enter_confirm_password_ID(self,confirm_text):
        self.driver.find_element(By.ID,self.confirm_password).click()
        self.driver.find_element(By.ID,self.confirm_password).clear()
        self.driver.find_element(By.ID,self.confirm_password).send_keys(confirm_text)

    def click_on_agree_check_box(self):
        self.driver.find_element(By.XPATH,self.agree_check_box_field).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button).click()
        return AccountSuccess(self.driver)

    def click_on_subscribe_button_Xpath(self):
        self.driver.find_element(By.XPATH,self.Subscribe_check_yes_XPATH).click()

    def Validate_Duplicate_email_entry_warning_message(self):
         wait = WebDriverWait(self.driver, 10)
         alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.Duplicate_email_entry_CSS_Selector)))
         return alert.text.strip()

    def validate_privacy_policy_message(self):
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.visibility_of_element_located((By.XPATH, self.Privacy_policy_warning_message_xpath)))
        return alert.text.strip()

    def validate_first_name_warning_message_xpath(self):
        return self.driver.find_element(By.XPATH,self.Expected_first_name_warning_message_xpath).text

    def validate_lastname_warning_message_xpath(self):
        return self.driver.find_element(By.XPATH,self.Expected_last_name_warning_message_xpath).text

    def validate_email_warning_message_xpath(self):
        return self.driver.find_element(By.XPATH,self.Expected_email_warning_message).text

    def validate_telephone_warning_message_xpath(self):
        return self.driver.find_element(By.XPATH,self.Expected_telephone_warning_message).text

    def validate_password_warning_message_xpath(self):
        return self.driver.find_element(By.XPATH,self.Expected_password_warning_message).text

    def register_with_mandatory_fields(self,first_name,last_name,email_text,telephone_number,password_text,confirm_text,yes_or_no,privacy_policy):
        self.enter_first_name_field_id(first_name)
        self.enter_last_name_field_ID(last_name)
        self.enter_email_field_ID(email_text)
        self.enter_telephone_number_ID(telephone_number)
        self.enter_password_ID(password_text)
        self.enter_confirm_password_ID(confirm_text)
        if yes_or_no.__eq__("yes"):
            self.click_on_subscribe_button_Xpath()
        if privacy_policy.__eq__("select"):
            self.click_on_agree_check_box()
        return self.click_on_continue_button()

    def verify_all_warning_message(self,expected_warning_message,expected2,expected3,expected4,expected5,expected6):
        actual_warning_message = self.validate_privacy_policy_message()
        actual_expected2 = self.validate_first_name_warning_message_xpath()
        actual_expected3 = self.validate_lastname_warning_message_xpath()
        actual_expected4 = self.validate_email_warning_message_xpath()
        actual_expected5 = self.validate_telephone_warning_message_xpath()
        actual_expected6= self.validate_password_warning_message_xpath()

        status = False

        if expected_warning_message.__eq__(actual_warning_message):
            if expected2.__eq__(actual_expected2):
                if expected3.__eq__(actual_expected3):
                    if expected4.__eq__(actual_expected4):
                        if expected5.__eq__(actual_expected5):
                            if expected6.__eq__(actual_expected6):
                                status = True
        return status





