from selenium.webdriver.common.by import By

from .base_page import BasePage


class CartPage(BasePage):
    ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT = (By.ID, "checkout")

    def item_count(self):
        return len(self.driver.find_elements(*self.ITEMS))

    def checkout(self):
        self.click(self.CHECKOUT)
