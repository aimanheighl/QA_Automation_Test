from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PropertySearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # --- Locators ---
    SEARCH_INPUT = (By.ID, "buy_keywords")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.button--search")

    # --- Actions ---

    def search(self, keyword: str):

        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(keyword)
        print(f"Search keyword entered: {keyword}")

        search_btn = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_btn.click()
        print("Search button clicked — waiting for results...")

        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "property__price")
            )
        )
        print("Search results loaded.")

    def get_property_price(self, index: int) -> str:
        """Return the price of the nth NON-EMPTY result (0-based)."""
        prices = [
            p.text.strip() for p in
            self.driver.find_elements(By.CLASS_NAME, "property__price")
            if p.text.strip()  # skip empty
        ]
        if index < len(prices):
            return prices[index]
        raise IndexError(f"No result at index {index} (only {len(prices)} non-empty)")

    def get_property_location(self, index: int) -> str:
        """Return the location of the nth NON-EMPTY result (0-based)."""
        locations = [
            loc.text.strip() for loc in
            self.driver.find_elements(By.CLASS_NAME, "property__location")
            if loc.text.strip()
        ]
        if index < len(locations):
            return locations[index]
        raise IndexError(f"No result at index {index} (only {len(locations)} non-empty)")

    def _get_bookmark_hearts(self):
        """Return all heart icons for non-empty results."""
        all_hearts = self.driver.find_elements(
            By.CSS_SELECTOR, "i.fa-heart.bookmark_heart"
        )

        return all_hearts

    def bookmark_property(self, index: int):

        hearts = self._get_bookmark_hearts()
        if index >= len(hearts):
            raise IndexError(f"No bookmark icon at index {index}")

        heart = hearts[index]
        self.driver.execute_script("arguments[0].click();", heart)
        print(f"Bookmarked result #{index + 1}")

        self.wait.until(
            lambda d: "fas" in hearts[index].get_attribute("class")
        )

    def is_bookmarked(self, index: int) -> bool:

        hearts = self.driver.find_elements(
            By.CSS_SELECTOR, "i.fa-heart.bookmark_heart"
        )
        if index >= len(hearts):
            return False

        return "fas" in hearts[index].get_attribute("class")