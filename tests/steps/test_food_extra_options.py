from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By

from locators.locators import MainPageLocators
from pages.extra_options_page import ExtraOptionsPage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils.usefull_elements import SignIn

scenarios('../features/test_food_extra_options.feature')


# background steps
@given('open the main page')
def load_page(browser):
    LoginPage(browser).load_page()
    LoginPage(browser).set_user_inputs()
    LoginPage(browser).click_delivery_button()
    print("\n---Step 1---Given---Pass---")


@when(parsers.cfparse('the user is logged in as "{username}"'))
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


# main steps
@given(parsers.cfparse('the user selects food name "{food}"'))
def select_food(browser, food):
    ExtraOptionsPage(browser).select_food(food=food)


@when('extra options container is displayed')
def check_container_is_displayed(browser):
    ExtraOptionsPage(browser).container_displayed()


@then(parsers.cfparse('the user selects the option "{option}"'))
def select_extra_option(browser, option):
    ExtraOptionsPage(browser).click_extra_options(option=option)


@then('the user closes the options container')
def close_container(browser):
    ExtraOptionsPage(browser).close_extra_options()


@then('the user clicks add button')
def click_add_button(browser):
    ExtraOptionsPage(browser).click_add_button()


@then('the alert message is displayed')
def get_alert_message(browser):
    assert ExtraOptionsPage(browser).get_alert_message() == 'Acest camp este obligatoriu'


@then(parsers.cfparse('the user clicks increase button for "{no_of_times}" times'))
def click_on_increase(browser, no_of_times):
    ExtraOptionsPage(browser).click_on_increase(no_of_times=no_of_times)


@then(parsers.cfparse('the value is increased by "{value}"'))
def check_increased_value(browser, value):
    assert int(ExtraOptionsPage(browser).get_current_quantity()) == 1 + int(value)


@then(parsers.cfparse('the user clicks decrease button for "{no_of_times}" times'))
def click_on_decrease(browser, no_of_times):
    old_qt = int(ExtraOptionsPage(browser).get_current_quantity())
    assert ExtraOptionsPage(browser).click_on_decrease(no_of_times=no_of_times) == old_qt - int(no_of_times)


@then(parsers.cfparse('the price is multiplied by "{no_of_times}" times when increasing quantity'))
def check_if_price_is_increased(browser, no_of_times):
    old_price = ExtraOptionsPage(browser).get_current_price()
    ExtraOptionsPage(browser).click_on_increase(no_of_times=no_of_times)
    assert ExtraOptionsPage(browser).get_current_price() == old_price * (1 + int(no_of_times))
