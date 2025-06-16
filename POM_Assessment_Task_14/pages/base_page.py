from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

# BasePage class to encapsulate common Selenium actions with explicit waits
class BasePage:
    def __init__(self, driver):
        self.driver = driver    # Initialize with WebDriver instance

    # Method to find an element with a specified locator and timeout
    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))  # Wait until element is present in the DOM
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.") # Handle case when element is not found in time
            return None

    # Method to find an element and click it
    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()

    # Method to enter text into an input field
    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear() # Clear any existing text in the input field
            element.send_keys(text) # Enter the specified text into the input field

    # Method to check if an element is displayed on the page
    def is_displayed(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.is_displayed() if element else False

    # Method to safely click an element, handling cases where the click might be intercepted
    def safe_click(self, locator):
        element = self.find_element(locator)
        try:
            element.click() # Attempt to click the element directly
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)    # Use JavaScript to click the element if the direct click fails
