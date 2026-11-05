Feature: Login
  As a shopper
  I want to authenticate on the store
  So that I can browse and buy products

  Background:
    Given I am on the login page

  Scenario: Successful login with a standard user
    When I log in as "standard_user" with password "secret_sauce"
    Then I should see the products page

  Scenario: Login is blocked for a locked-out user
    When I log in as "locked_out_user" with password "secret_sauce"
    Then I should see the error "Epic sadface: Sorry, this user has been locked out."

  Scenario: Login requires a password
    When I log in as "standard_user" with password ""
    Then I should see the error "Epic sadface: Password is required"
