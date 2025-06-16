from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Page Object Model class for the Login Page of the Zen Portal
class LoginPage(BasePage):
    # Locators for the login page elements
    USERNAME_INPUT = (By.ID,":r0:")  # Locator for username input field            
    PASSWORD_INPUT = (By.ID,":r1:")  # Locator for password input field
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']") # Locator for submit button
    DASHBOARD_ELEMENT = (By.ID, "profile-click-icon")   # Locator for dashboard/profile icon after successful login
    ERROR_MESSAGE = (By.ID, ":r1:-helper-text")         # Locator for error message displayed on failed login
    
    # Method to perform login using provided username and password
    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)      # Enter username
        self.enter_text(self.PASSWORD_INPUT, password)      # Enter password
        self.click(self.SUBMIT_BUTTON)                      # Click the submit button to log in

    # Method to perform logout by clicking on the profile icon and selecting logout option
    def logout(self):
        self.safe_click((By.XPATH, "//div[@class='avatar-main-div d-flex cursor mock-interview']//div//img[@alt='D']"))
        self.safe_click((By.XPATH, "//div[normalize-space()='Log out']"))

    # Check if username field is present on the page
    def is_username_field_present(self):
        return self.is_displayed(self.USERNAME_INPUT)

    # Check if password field is present on the page
    def is_password_field_present(self):
        return self.is_displayed(self.PASSWORD_INPUT)

    # Check if submit button is present on the page
    def is_submit_button_present(self):
        return self.is_displayed(self.SUBMIT_BUTTON)

    # Check if login was successful by verifying the presence of the dashboard element
    def is_login_successful(self):
        return self.is_displayed(self.DASHBOARD_ELEMENT)

    # Check if an error message is displayed for failed login attempts
    def is_login_error_present(self):
        return self.is_displayed(self.ERROR_MESSAGE)
    
    # Check if the logout button is present on the page
    def is_logout_button_present(self):
        return self.is_displayed((By.XPATH, "//div[@class='avatar-main-div d-flex cursor mock-interview']//div//img[@alt='D']"))
        