from selenium.webdriver.common.by import By

from .base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def add_item(self, item_id):
        self.click((By.CSS_SELECTOR, f"[data-test='add-to-cart-{item_id}']"))

    def remove_item(self, item_id):
        self.click((By.CSS_SELECTOR, f"[data-test='remove-{item_id}']"))

    def cart_count(self):
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)
