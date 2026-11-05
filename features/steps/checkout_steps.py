from behave import given, when, then

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@given("I go to the cart")
@when("I go to the cart")
def step_go_to_cart(context):
    InventoryPage(context.driver).go_to_cart()
    context.cart = CartPage(context.driver)


@when("I proceed to checkout")
def step_proceed_checkout(context):
    context.cart.checkout()
    context.checkout = CheckoutPage(context.driver)


@when('I fill the checkout info with "{first:w}" "{last:w}" "{postal:w}"')
def step_fill_info(context, first, last, postal):
    context.checkout.fill_info(first, last, postal)


@when("I finish the order")
def step_finish_order(context):
    context.checkout.finish()


@then('I should see the confirmation "{message}"')
def step_confirmation(context, message):
    assert message in context.checkout.confirmation()
