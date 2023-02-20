Feature: Test menu buttons

  Scenario Outline: Verify menu buttons
    Given open the main page
    And the user is logged in as "ionionica"
    When the user clicks "<button>" named "<name>"
    Then the user is redirected to "<page>"

    Examples: button, name, page
      | button         | name            | page                                                    |
      | KIMPOLUNG      | KIMPOLUNG       | https://www.restaurantbucovina.ro/menu?categoryID=69247 |
      | Recomandări    | Recomandări     | https://www.restaurantbucovina.ro/menu?categoryID=70211 |
      | Promoții Combo | Promoții Combo  | https://www.restaurantbucovina.ro/menu?categoryID=50933 |
      | Mic Dejun      | Mic Dejun       | https://www.restaurantbucovina.ro/menu?categoryID=63894 |
      | Gustări        | Gustări         | https://www.restaurantbucovina.ro/menu?categoryID=63902 |
      | Ciorbe         | Ciorbe          | https://www.restaurantbucovina.ro/menu?categoryID=63893 |
      | Salate Aperitiv| Salate Aperitiv | https://www.restaurantbucovina.ro/menu?categoryID=63947 |
      | Tradiționale   | Tradiționale    | https://www.restaurantbucovina.ro/menu?categoryID=63944 |
      | Carne de Pui   | Carne de Pui    | https://www.restaurantbucovina.ro/menu?categoryID=77498 |
      | Carne de Porc  | Carne de Porc   | https://www.restaurantbucovina.ro/menu?categoryID=77499 |
      | Carne de Vită  | Carne de Vită   | https://www.restaurantbucovina.ro/menu?categoryID=77500 |
      | Vegans & Post  | Vegans & Post   | https://www.restaurantbucovina.ro/menu?categoryID=63946 |
      | More...        | More...         | https://www.restaurantbucovina.ro/menu                  |
