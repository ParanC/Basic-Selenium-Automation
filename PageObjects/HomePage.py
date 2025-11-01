from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.LoginPage import LoginPage
from PageObjects.RegisterPage import RegisterPage
from PageObjects.SearchPage_items import SearchPageItems



class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    search_box_field ="search"
    search_button_Xpath="//button[contains(@class,'btn-default')]"
    my_account_xpath = "//span[text()='My Account']"
    login_option ="Login"
    register_option_Link_text ="Register"
    def enter_Product_name_into_Search(self,product_name):
        self.driver.find_element(By.NAME, self.search_box_field).click()
        self.driver.find_element(By.NAME, self.search_box_field).clear()
        self.driver.find_element(By.NAME,self.search_box_field).send_keys(product_name)
    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_Xpath).click()
        return SearchPageItems(self.driver)
    def click_on_my_account_drop_down(self):
        self.driver.find_element(By.XPATH,self.my_account_xpath).click()
    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option).click()
        return LoginPage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_down()
        return self.click_on_login_option()

    def click_on_register_option(self):
        self.driver.find_element(By.LINK_TEXT,self.register_option_Link_text).click()
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_down()
        return self.click_on_register_option()

    def Search_for_a_product(self,product_name):
        self.enter_Product_name_into_Search(product_name)
        self.click_on_search_button()
        return SearchPageItems(self.driver)


