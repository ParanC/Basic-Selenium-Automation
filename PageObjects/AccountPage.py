from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self,driver):
        self.driver = driver

    account_Page_link_text = "Edit your account information"
    def account_page_link_text_verify(self):
        return self.driver.find_element(By.LINK_TEXT,self.account_Page_link_text).is_displayed()
