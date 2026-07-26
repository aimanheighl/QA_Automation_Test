from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    FIRST_NAME = (By.ID, "name")
    LAST_NAME = (By.ID, "last_name")
    MOBILE_NO = (By.ID, "mobile_no")
    DATE_OF_BIRTH = (By.ID, "date_of_birth")

    NEWSLETTER = (By.ID, "newsletter")
    PROPERTY_AGENT = (By.ID, "category")

    AGENCY_ECODE = (By.ID, "ecode")
    REN_CODE = (By.ID, "ren_code")

    BUSINESS_CARD = (By.ID, "business_card")

    REGISTER_BUTTON = (By.ID, "submit-btn")
    TERMS_CONDITIONS = (By.LINK_TEXT, "Terms and Conditions")
    PRIVACY_POLICY = (By.LINK_TEXT, "Privacy Policy")

    def enter_email(self, email):

        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )

        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):

        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )

        password_field.clear()
        password_field.send_keys(password)

    def enter_first_name(self, first_name):

        first_name_field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )

        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):

        last_name_field = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )

        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_mobile_number(self, mobile_number):

        mobile_field = self.wait.until(
            EC.visibility_of_element_located(self.MOBILE_NO)
        )

        mobile_field.clear()
        mobile_field.send_keys(mobile_number)

    def enter_date_of_birth(self, date_of_birth):

        date_field = self.wait.until(
            EC.presence_of_element_located(self.DATE_OF_BIRTH)
        )

        self.driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', {bubbles:true}));
            arguments[0].dispatchEvent(new Event('change', {bubbles:true}));
        """, date_field, date_of_birth)

        print(f"Date of Birth set to: {date_of_birth}")

    def select_property_agent(self):

        property_agent = self.wait.until(
            EC.presence_of_element_located(self.PROPERTY_AGENT)
        )

        if not property_agent.is_selected():

            self.driver.execute_script(
                "arguments[0].click();",
                property_agent
            )

    def disable_newsletter(self):

        newsletter = self.wait.until(
            EC.presence_of_element_located(self.NEWSLETTER)
        )

        if newsletter.is_selected():

            self.driver.execute_script(
                "arguments[0].click();",
                newsletter
            )


    def enter_agency_ecode(self, ecode):

        ecode_field = self.wait.until(
            EC.visibility_of_element_located(self.AGENCY_ECODE)
        )

        ecode_field.clear()
        ecode_field.send_keys(ecode)

    def enter_ren_code(self, ren_code):

        ren_field = self.wait.until(
            EC.visibility_of_element_located(self.REN_CODE)
        )

        ren_field.clear()
        ren_field.send_keys(ren_code)

    def upload_business_card(self, file_path):

        file_input = self.wait.until(
            EC.presence_of_element_located(self.BUSINESS_CARD)
        )

        file_input.send_keys(file_path)

        print("Business card uploaded.")

    def is_newsletter_disabled(self):

        newsletter = self.driver.find_element(
            *self.NEWSLETTER
        )

        return not newsletter.is_selected()

    def is_property_agent_selected(self):

        property_agent = self.driver.find_element(
            *self.PROPERTY_AGENT
        )

        return property_agent.is_selected()

    def get_email_value(self):

        return self.driver.find_element(
            *self.EMAIL
        ).get_attribute("value")

    def get_first_name_value(self):

        return self.driver.find_element(
            *self.FIRST_NAME
        ).get_attribute("value")

    def get_last_name_value(self):

        return self.driver.find_element(
            *self.LAST_NAME
        ).get_attribute("value")

    def get_mobile_number_value(self):

        return self.driver.find_element(
            *self.MOBILE_NO
        ).get_attribute("value")

    def get_agency_ecode_value(self):

        return self.driver.find_element(
            *self.AGENCY_ECODE
        ).get_attribute("value")

    def get_ren_code_value(self):

        return self.driver.find_element(
            *self.REN_CODE
        ).get_attribute("value")

    def do_not_submit(self):

        print(
            "Registration form prepared successfully. "
            "Register button will NOT be clicked."
        )

    def click_privacy_policy_and_close(self):

        main_window = self.driver.current_window_handle

        privacy_link = self.wait.until(
            EC.element_to_be_clickable(self.PRIVACY_POLICY)
        )
        privacy_link.click()
        print("Clicked Privacy Policy")

        self.wait.until(EC.number_of_windows_to_be(2))
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        print("Switched to Privacy Policy tab — closing it")
        self.driver.close()
        self.driver.switch_to.window(main_window)
        print("Returned to Registration page")

    def click_terms_and_conditions(self):

        main_window = self.driver.current_window_handle

        tc_link = self.wait.until(
            EC.element_to_be_clickable(self.TERMS_CONDITIONS)
        )
        tc_link.click()
        print("Clicked Terms & Conditions")

        self.wait.until(EC.number_of_windows_to_be(2))
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        print("Switched to Terms & Conditions tab — leaving it open")
        self.driver.switch_to.window(main_window)  # back to registration
        print("Returned to Registration page (T&C tab remains open)")