from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    # Method to locate username and password web elements and pass data into it and login
    def login(self, username, password):

        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input.send_keys(password)

        login_button = (WebDriverWait
                        (self.driver, 10).until
                        (EC.visibility_of_element_located
                         ((By.XPATH,
                           "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"))))
        login_button.click()

        # Checks if the substring dashboard is present in current url
        if "dashboard" in self.driver.current_url:
            return True
        else:
            return False
