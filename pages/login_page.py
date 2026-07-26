from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    LOGIN_BUTTON = (By.ID, "log-txt")

    def click_login(self):

        print("Waiting for Login button...")

        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )

        print("Login button found:", login_button.text)

        login_button.click()

        print("Login button clicked successfully")

    def click_create_account(self):

        print("Waiting for Create an Account...")

        create_account = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(translate(normalize-space(text()), "
                    "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
                    "'abcdefghijklmnopqrstuvwxyz'), "
                    "'create an account')]"
                )
            )
        )

        print(
            "Create Account found:",
            create_account.text
        )

        create_account.click()

        print("Create Account clicked successfully")

    def login(self, email: str, password: str):

        email_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_field.clear()
        email_field.send_keys(email)
        print(f"Email entered: {email}")

        password_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)
        print("Password entered")

        login_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Login')]")
            )
        )
        login_btn.click()
        print("Login button clicked — waiting for redirect...")