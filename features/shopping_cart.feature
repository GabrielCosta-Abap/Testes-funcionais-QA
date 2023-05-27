Feature: Shopping Cart

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"

  Scenario: Add an item to the shopping cart
    When I select an item named "Sauce Labs Backpack"
    And I add the item to the shopping cart
    Then the item is displayed in the shopping cart

  Scenario: Remove an item from the cart
    When I add an item to the cart
    And I remove the item from the cart
    Then The item should be removed from the cart

  Scenario: View details of an item
    When I click on an item
    Then I should see the item details

  Scenario: Empty the cart
    When I add items to the cart
    And I empty the cart
    Then The cart should be empty

  Scenario: Proceed to checkout
    When I add an item to the cart
    And I proceed to checkout
    Then I should be redirected to the checkout page