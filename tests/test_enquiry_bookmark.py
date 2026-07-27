import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver import create_driver
from utils.test_data import LOGIN_USER
from utils.logger import get_logger

from pages.login_page import LoginPage
from pages.property_search_page import PropertySearchPage

logger = get_logger(__name__)


def test_enquiry_and_bookmark_flow():

    driver = create_driver()

    try:
        logger.info("=" * 50)
        logger.info("TEST CASE 2: Enquiry & Bookmark Flow")
        logger.info("=" * 50)

        driver.get("https://www.starproperty.my/")

        login_page = LoginPage(driver)
        login_page.click_login()
        login_page.login(
            email=LOGIN_USER["email"],
            password=LOGIN_USER["password"],
        )

        wait = WebDriverWait(driver, 20)

        logo = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "starproperty_dashboard_logo")
            )
        )
        logo.click()
        logger.info("Navigated from Dashboard → Homepage")

        to_buy = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "To Buy"))
        )
        driver.execute_script("arguments[0].click();", to_buy)
        logger.info("'To Buy' tab selected")

        search_page = PropertySearchPage(driver)
        search_page.search("Kuala Lumpur")

        for i in range(2):
            price = search_page.get_property_price(i)
            location = search_page.get_property_location(i)
            logger.info(f"Property #{i + 1}: {price} | {location}")

        for i in range(2):
            search_page.bookmark_property(i)
        logger.info("First 2 properties bookmarked")

        time.sleep(2)

        driver.get(
            "https://www.starproperty.my/bookmark/all_bookmark"
            "?type=classifieds"
        )
        logger.info("Navigated to Bookmarks page")

        bookmark_items = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".bookmark__title, h4.bookmark__title")
            )
        )
        assert len(bookmark_items) >= 2, (
            f"Expected at least 2 bookmarks, found {len(bookmark_items)}"
        )
        logger.info(f"Bookmarked records on page: {len(bookmark_items)}")

        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, "input.fill-control-input"
        )
        assert len(checkboxes) >= 2, (
            f"Expected at least 2 checkboxes, found {len(checkboxes)}"
        )
        for i in range(2):
            if not checkboxes[i].is_selected():
                driver.execute_script(
                    "arguments[0].click();", checkboxes[i]
                )
        logger.info("Selected first 2 bookmarked records")

        compare_btn = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "compareList_classifieds")
            )
        )
        driver.execute_script("arguments[0].click();", compare_btn)
        logger.info("Compare button clicked")

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[id^='compareEnquiries_classifieds']")
            )
        )
        logger.info("Compare page fully loaded")

        enquiry_buttons = driver.find_elements(
            By.CSS_SELECTOR,
            "[id^='compareEnquiries_classifieds'], "
            ".sendEnquiryCompare, "
            "div.button--enquiry"
        )
        logger.info(f"Send Enquiry buttons found: {len(enquiry_buttons)}")

        assert len(enquiry_buttons) >= 2, (
            f"Expected at least 2 Send Enquiry buttons, "
            f"found {len(enquiry_buttons)}"
        )

        driver.execute_script(
            "arguments[0].click();", enquiry_buttons[1]
        )
        logger.info("Clicked 'Send Enquiries' for 2nd record")

        name_field = wait.until(
            EC.visibility_of_element_located((By.ID, "enquiry_name"))
        )
        name_field.clear()
        name_field.send_keys("Aiman Azmi")
        logger.info("Name entered")

        phone_field = driver.find_element(By.ID, "enquiry_phone")
        phone_field.clear()
        phone_field.send_keys("+60123456789")
        logger.info("Phone entered")

        email_field = driver.find_element(By.ID, "enquiry_email")
        email_field.clear()
        email_field.send_keys("aimanazmi@example.com")
        logger.info("Email entered")

        logger.info("Enquiry form populated — will NOT submit")

        close_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.close[data-dismiss='modal']")
            )
        )
        close_btn.click()

        logger.info("Cleaning up bookmarked items...")

        driver.get(
            "https://www.starproperty.my/bookmark/all_bookmark?type=classifieds"
        )

        bookmark_items = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".bookmark__title, h4.bookmark__title")
            )
        )

        logger.info(f"Bookmarks found for cleanup: {len(bookmark_items)}")

        if bookmark_items:

            item_checkboxes = driver.find_elements(
                By.CSS_SELECTOR,
                "input.fill-control-input:not(#list_classifieds)"
            )

            logger.info(f"Checkboxes found: {len(item_checkboxes)}")

            for checkbox in item_checkboxes:
                if not checkbox.is_selected():
                    driver.execute_script(
                        "arguments[0].click();",
                        checkbox
                    )
                    time.sleep(0.5)

            logger.info("Selected all bookmark checkboxes")

            time.sleep(2)

            clear_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "removeBookmark_classifieds")
                )
            )

            driver.execute_script(
                "arguments[0].click();",
                clear_btn
            )

            logger.info("Clicked Clear")

            time.sleep(3)

            driver.refresh()
            time.sleep(2)

            visible_bookmarks = [
                item for item in driver.find_elements(
                    By.CSS_SELECTOR,
                    ".bookmark__title, h4.bookmark__title"
                )
                if item.is_displayed()
            ]

            if len(visible_bookmarks) == 0:
                logger.info("Bookmarks cleared successfully")
            else:
                logger.warning(
                    f"{len(visible_bookmarks)} visible bookmark(s) remain"
                )

        logger.info("Enquiry form closed — not submitted")

        dashboard_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "log-txt"))
        )
        dashboard_btn.click()
        logger.info("Opened Dashboard dropdown")

        logout_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
        )
        logout_link.click()
        logger.info("Logged out successfully")

        logger.info("=" * 50)
        logger.info("TEST CASE 2 PASSED: Enquiry & Bookmark Flow")
        logger.info("=" * 50)

    finally:
        driver.quit()