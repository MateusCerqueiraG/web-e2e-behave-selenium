Feature: Shopping cart
  As a logged-in shopper
  I want to manage products in my cart
  So that I buy exactly what I want

  Background:
    Given I am logged in as a standard user

  Scenario: Adding a product updates the cart badge
    When I add the "sauce-labs-backpack" to the cart
    Then the cart badge should show "1"

  Scenario: Removing a product empties the cart
    Given I add the "sauce-labs-backpack" to the cart
    When I remove the "sauce-labs-backpack" from the cart
    Then the cart should be empty
