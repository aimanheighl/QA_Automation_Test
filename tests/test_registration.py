import os
from datetime import datetime

from selenium.webdriver.common.by import By

from utils.driver import create_driver
from utils.test_data import TEST_USER
from utils.logger import get_logger

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

logger = get_logger(__name__)

def test_open_registration_page():

    driver = create_driver()

    try:

        logger.info("=" * 50)
        logger.info("TEST STARTED: User Registration Flow")
        logger.info("=" * 50)

        driver.get(
            "https://www.starproperty.my/"
        )

        login_page = LoginPage(driver)
        login_page.click_login()
        login_page.click_create_account()
        registration_page = RegistrationPage(driver)

        registration_page.enter_first_name(
            TEST_USER["first_name"]
        )

        registration_page.enter_last_name(
            TEST_USER["last_name"]
        )

        registration_page.enter_email(
            TEST_USER["email"]
        )

        registration_page.enter_password(
            TEST_USER["password"]
        )

        logger.info(f"Generated phone: {TEST_USER['phone']}")
        registration_page.enter_mobile_number(TEST_USER["phone"])

        registration_page.enter_date_of_birth(
            TEST_USER["date_of_birth"]
        )

        registration_page.select_property_agent()
        registration_page.disable_newsletter()


        registration_page.enter_agency_ecode(
            TEST_USER["agency_ecode"]
        )

        registration_page.enter_ren_code(
            TEST_USER["ren_code"]
        )

        business_card_path = os.path.abspath(
            "test_data/business_card.png"
        )

        registration_page.upload_business_card(
            business_card_path
        )

        uploaded_file = driver.find_element(
            By.ID,
            "business_card"
        ).get_attribute("value")

        logger.info(f"Uploaded File: {uploaded_file}")

        assert "business_card.png" in uploaded_file

        assert (
                registration_page.get_first_name_value()
                == TEST_USER["first_name"]
        )

        assert (
                registration_page.get_last_name_value()
                == TEST_USER["last_name"]
        )

        assert (
                registration_page.get_email_value()
                == TEST_USER["email"]
        )

        ...

        assert (
            registration_page.get_first_name_value()
            == TEST_USER["first_name"]
        )

        assert (
            registration_page.get_last_name_value()
            == TEST_USER["last_name"]
        )

        assert (
            registration_page.get_email_value()
            == TEST_USER["email"]
        )

        assert (
            registration_page.get_mobile_number_value()
            == TEST_USER["phone"]
        )

        assert (
            registration_page.is_property_agent_selected()
        )

        assert (
            registration_page.is_newsletter_disabled()
        )

        assert (
            registration_page.get_agency_ecode_value()
            == TEST_USER["agency_ecode"]
        )

        assert (
                registration_page.get_ren_code_value()
                == TEST_USER["ren_code"]
        )

        registration_page.click_privacy_policy_and_close()
        registration_page.click_terms_and_conditions()

        assert (
                registration_page.get_first_name_value()
                == TEST_USER["first_name"]
        )

        assert (
                registration_page.get_email_value()
                == TEST_USER["email"]
        )

        registration_page.do_not_submit()

        logger.info(
            "TEST PASSED: Registration form fully populated, "
            "Privacy Policy closed, Terms & Conditions left open, "
            "form never submitted."
        )

        logger.info(
            "TEST PASSED: Registration form "
            "fully populated without submission."
        )


    except Exception:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot = os.path.join("logs", f"FAILURE_{timestamp}.png")

        driver.save_screenshot(screenshot)

        logger.error(f"SCREENSHOT SAVED: {screenshot}")

        logger.exception("TEST FAILED — see screenshot above")

        raise


    finally:

        driver.quit()

        logger.info("Browser closed.")