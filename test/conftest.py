import pytest
from selenium import webdriver
from Utilities import ReadConfigurations


@pytest.fixture()
def setup_and_tearDown_code(request):
    browser = ReadConfigurations.read_configurations("basic info","browser")
    driver = None
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        print("Please provide a valid browser from the list -- Chrome/FireFox/Edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configurations("basic info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()

