from selenium.webdriver.common.by import By

class AccountSuccess:
    def __init__(self,driver):
        self.driver = driver
    AccountSuccess_css_selector =" div#content h1 "
    def accountSuccess_status_verify(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.AccountSuccess_css_selector).text