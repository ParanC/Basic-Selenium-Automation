from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchPageItems:
    def __init__(self,driver):
        self.driver = driver
    valid_hp_product_link_text ="HP LP3065"
    no_product_message_xpath ="//input[@id='button-search']/following-sibling::p"
    def status_hp_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_hp_product_link_text).is_displayed()
    def no_such_product_retrieved(self):
        return self.driver.find_element(By.XPATH,self.no_product_message_xpath).text