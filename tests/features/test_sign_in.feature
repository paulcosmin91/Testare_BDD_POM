Feature: Test login functionality

  Scenario: Login successfully
    Given open the authentication page
    When the user types username "abracadabra@yahoo.com"
    And the user types password "testare"
    And the user clicks the signin button
    Then the user is redirected to main page
    And the user is logged in as "ionionica"

  Scenario Outline: Login unsuccessfully
    Given open the authentication page
    When the user types username "<username>"
    And the user types password "<password>"
    And the user clicks the signin button
    Then the user stayed on the authentication page
    And the error "<error>" message of "<error_type>" is displayed

    Examples: usernames, passwords and errors
      | username                | password | error                            | error_type     |
      | alfaDaniel@yahoo.com    | 12r43td  | Utilizator sau Parola Incorecte. | login_error    |
      | abracadabra@yahoo.com   | 1234     | Utilizator sau Parola Incorecte. | login_error    |
      | testDani@yahoo.com      | /        | Acest camp este obligatoriu      | password_error |
      | testDaniel              | 123456   | Adresa email invalida.           | email_error    |
      | /                       | 123456   | Acest camp este obligatoriu      | email_error    |
    # Figured out that "/" is fed as blank space to the site
