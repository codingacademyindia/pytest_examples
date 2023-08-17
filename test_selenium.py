import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Fixture to initialize the browser
@pytest.fixture
def browser():
    # You can replace 'chromedriver.exe' with the path to your Chrome WebDriver executable
    driver = webdriver.Chrome('driver/chromedriver.exe')
    yield driver
    driver.quit()

# Test function to interact with a web page
def test_web_interaction(browser):
    # Open a web page
    browser.get("https://www.google.com")

    # Perform interactions
    assert "Google" in browser.title

    # Find an element and interact with it
    search_box = browser.find_element("name", "q")
    search_box.clear()
    search_box.send_keys("Pytest with Selenium")
    search_box.send_keys(Keys.RETURN)

    # Assertion for search result
    assert "No results found." not in browser.page_source
