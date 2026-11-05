from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def _click_until(self, button, settled, attempts=5, poll_timeout=6):
        """SauceDemo's React form occasionally drops the first submit click,
        leaving the page on the same step with no error. Re-click until the
        page actually settles into the expected state."""
        last_error = None
        for _ in range(attempts):
            self.click(button)
            try:
                WebDriverWait(self.driver, poll_timeout).until(settled)
                return
            except TimeoutException as exc:
                last_error = exc
        raise last_error

    def fill_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self._click_until(
            self.CONTINUE,
            lambda d: "checkout-step-two" in d.current_url or d.find_elements(*self.ERROR),
        )

    def finish(self):
        self._click_until(
            self.FINISH,
            lambda d: bool(d.find_elements(*self.COMPLETE_HEADER)),
        )

    def confirmation(self):
        return self.text_of(self.COMPLETE_HEADER)
