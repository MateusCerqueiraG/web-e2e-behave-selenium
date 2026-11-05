"""Steps shared across features (kept here so there is a single definition)."""
from behave import then
from selenium.webdriver.common.by import By


@then('I should see the error "{message}"')
def step_see_error(context, message):
    element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert message in element.text, f"Expected error '{message}', got '{element.text}'"
