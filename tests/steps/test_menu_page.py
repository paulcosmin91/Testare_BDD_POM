from pytest_bdd import scenarios, given, when, then, parsers


from locators.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils.usefull_elements import SignIn
from selenium.webdriver.common.by import By

scenarios('../features/test_menu_page.feature')


@given('open the main page')
def load_page(browser):
    LoginPage(browser).load_page()
    LoginPage(browser).set_user_inputs()
    LoginPage(browser).click_delivery_button()
    print("\n---Step 1---Given---Pass---")


@given(parsers.cfparse('the user is logged in as "{username}"'))
def check_user_name_displayed(browser):
    assert MenuPage(browser).get_account_name() == SignIn.TEST_USERNAME
    print("\n---Step 2---Given---Pass---")


@when(parsers.cfparse('the user clicks "{button}" named "{name}"'))
def check_button_name_and_click_it(browser, button, name):
    button_name = browser.find_element(By.XPATH, f"{MainPageLocators.menu_button.format(button)}").text
    assert button_name == name
    MenuPage(browser).click_menu_buttons(button_name=name)
    print("\n---Step 3---When---Pass---")


@then(parsers.cfparse('the user is redirected to "{page}"'))
def check_user_redirected_to_page(browser, page):
    assert browser.current_url == page, "Main page URL is not ok."
    print("\n---Step 4---Then---Pass---")
