import pytest
from selenium.webdriver.common.by import By

from PageObjects.SearchPage_items import SearchPageItems
from PageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_tearDown_code")
class TestSearch:

    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.Search_for_a_product("HP")

        assert search_page.status_hp_product()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        SearchPage_items  = home_page.Search_for_a_product("HONDA")


        expected_text ="There is no product that matches the search criteria."

        assert SearchPage_items.no_such_product_retrieved().__eq__(expected_text)


    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        SearchPage_items = home_page.Search_for_a_product("")
        expected_text ="There is no product that matches the search criteria."
        assert SearchPage_items.no_such_product_retrieved().__eq__(expected_text)






