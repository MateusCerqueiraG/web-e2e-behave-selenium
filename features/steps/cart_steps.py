from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("I am logged in as a standard user")
def step_logged_in(context):
    login = LoginPage(context.driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    context.inventory = InventoryPage(context.driver)
    assert context.inventory.is_loaded(), "Login did not reach the inventory page"


@given('I add the "{item}" to the cart')
@when('I add the "{item}" to the cart')
def step_add_item(context, item):
    context.inventory.add_item(item)


@when('I remove the "{item}" from the cart')
def step_remove_item(context, item):
    context.inventory.remove_item(item)


@then('the cart badge should show "{count}"')
def step_cart_badge(context, count):
    assert context.inventory.cart_count() == int(count)


@then("the cart should be empty")
def step_cart_empty(context):
    assert context.inventory.cart_count() == 0
