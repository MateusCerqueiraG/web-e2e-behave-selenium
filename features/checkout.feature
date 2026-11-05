Feature: Checkout
  As a logged-in shopper
  I want to complete my purchase
  So that my order is placed

  Background:
    Given I am logged in as a standard user
    And I add the "sauce-labs-backpack" to the cart
    And I go to the cart

  Scenario: Complete a purchase end to end
    When I proceed to checkout
    And I fill the checkout info with "Mateus" "Cerqueira" "70000-000"
    And I finish the order
    Then I should see the confirmation "Thank you for your order!"

  Scenario: Checkout requires customer information
    When I proceed to checkout
    And I fill the checkout info with "" "" ""
    Then I should see the error "Error: First Name is required"
