from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("I am on the login page")
def step_open_login(context):
    context.login = LoginPage(context.driver)
    context.login.load()


@when('I log in as "{username}" with password "{password:w}"')
def step_login(context, username, password):
    context.login.login(username, password)


@then("I should see the products page")
def step_products_page(context):
    inventory = InventoryPage(context.driver)
    assert inventory.is_loaded(), f"Expected inventory page, got {context.driver.current_url}"
    assert inventory.is_visible(InventoryPage.TITLE)
