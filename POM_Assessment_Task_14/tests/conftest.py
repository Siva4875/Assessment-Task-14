import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Pytest fixture to initialize and provide the WebDriver instance to tests
@pytest.fixture
def driver(request):
        chrome_options = Options()                  # Create ChromeOptions instance to customize browser behavior
        chrome_options.add_argument("--incognito")  # Launch the Chrome browser in incognito mode for clean sessions

        driver = webdriver.Chrome(options=chrome_options) # Initialize the Chrome WebDriver with the specified options
        driver.get("https://www.zenclass.in/login")       # Navigate to the Zen Class login page
        driver.maximize_window()                  # Maximize the browser window for better visibility during testing
        request.cls.driver = driver               # Attach the WebDriver instance to the test class (useful for class-based tests)
        yield driver                              # Provide the WebDriver instance to the test
        driver.quit()                             # Quit the browser after the test is done        