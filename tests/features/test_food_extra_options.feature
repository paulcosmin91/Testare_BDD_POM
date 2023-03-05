Feature: Test extra options

  Background:
    Given open the main page
    When the user is logged in as "ionionica"
    And the user clicks "Ciorbe" named "Ciorbe"
    Then the user is redirected to "https://www.restaurantbucovina.ro/menu?categoryID=63893"

  Scenario Outline: Verify food options for ciorbe
    Given the user selects food name "<food>"
    When extra options container is displayed
    Then the user selects the option "<option>"
    And the user closes the options container

    Examples: food, option
      | food    | option            |
      | Legume  | Lingură           |
      | Legume  | Nu doresc lingură |
      | Legume  | Ardei iute        |
      | Legume  | Mujdei            |
      | Legume  | Smântână          |

  Scenario: Verify mandatory option is required
    Given the user selects food name "Burtă"
    When extra options container is displayed
    Then the user clicks add button
    And the alert message is displayed

  Scenario: Verify increase and decrease buttons
    Given the user selects food name "Burtă"
    When extra options container is displayed
    Then the user clicks increase button for "3" times
    And the value is increased by "3"
    And the user clicks decrease button for "2" times

  Scenario: Verify the price when increasing quantity
    Given the user selects food name "Burtă"
    When extra options container is displayed
    Then the price is multiplied by "3" times when increasing quantity