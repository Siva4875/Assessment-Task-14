from pages.login_page import LoginPage

class TestLogin:
    # Test cases for ZenClass login functionality
    # Below are the test cases for the ZenClass Sucessful login Functionality
    def test_successful_login_logout(self, driver):
        driver.get("https://www.zenclass.in/login")
        login_page = LoginPage(driver)
        login_page.login("ValidUsername@gmail.com", "ValidPassword")  # Replace with actual valid credentials
        # Assert that login was successful by checking for the presence of the dashboard element
        assert login_page.is_login_successful(), "Login failed!"
        login_page.logout()
        assert login_page.is_username_field_present(), "Logout failed!"

    # Below are the test cases for the ZenClass Unsucessful login Functionality
    def test_unsuccessful_login(self, driver):
        driver.get("https://www.zenclass.in/login")
        login_page = LoginPage(driver)
        login_page.login("invaliduser@gmail.com", "wrong_pass")

        assert login_page.is_login_error_present(), "Error not displayed for invalid login!"

    # Below are the test cases for the ZenClass login page elements to Validate the Username and Password inputbox
    def test_username_password_fields(self, driver):
        driver.get("https://www.zenclass.in/login")
        login_page = LoginPage(driver)
        assert login_page.is_username_field_present(), "Username field missing!"
        assert login_page.is_password_field_present(), "Password field missing!"

    # Below are the test cases for the ZenClass login page elements to Validate the Submit button
    def test_submit_button(self, driver):
        driver.get("https://www.zenclass.in/login")
        login_page = LoginPage(driver)
        assert login_page.is_submit_button_present(), "Submit button missing!"

    # Below are the test cases for the ZenClass login page elements to Validate the Logout button
    def test_logout_button(self, driver):
        driver.get("https://www.zenclass.in/login")
        login_page = LoginPage(driver)
        login_page.login("validusername@gmail.com", "ValidPassword") # Replace with actual valid credentials
        # Assert that login was successful by checking for the presence of the dashboard element
        assert login_page.is_logout_button_present(), "Logout button missing!"
        login_page.logout()
        assert login_page.is_username_field_present(), "Logout failed!"

