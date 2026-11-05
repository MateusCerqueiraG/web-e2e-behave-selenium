"""Behave hooks: driver lifecycle, cross-browser selection and failure screenshots."""
import os
import sys

# Put the features/ dir on the path so steps can `from pages.x import Y`
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import allure
import parse
from behave import register_type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Custom type so Gherkin params may be empty ("") — e.g. empty password / blank form.
@parse.with_pattern(r'[^"]*')
def parse_maybe_empty(text):
    return text


register_type(w=parse_maybe_empty)


def _make_driver():
    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    driver.set_window_size(1366, 768)
    return driver


def before_scenario(context, scenario):
    context.driver = _make_driver()


def after_step(context, step):
    driver = getattr(context, "driver", None)
    if step.status == "failed" and driver is not None:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"screenshot-{step.name}",
            attachment_type=allure.attachment_type.PNG,
        )


def after_scenario(context, scenario):
    driver = getattr(context, "driver", None)
    if driver is not None:
        driver.quit()
