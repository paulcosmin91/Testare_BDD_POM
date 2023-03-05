import time

from selenium.webdriver.common.by import By

from locators.locators import ExtraOptionsLocators, MainPageLocators


class ExtraOptionsPage:
    def __init__(self, browser):
        self.browser = browser

    def click_extra_options(self, option):
        self.browser.find_element(By.XPATH, f"{ExtraOptionsLocators.checkbox.format(option)}").click()
        print(f"\nClicked on option {option}!")

    def select_food(self, food):
        self.browser.find_element(By.XPATH, f"{MainPageLocators.food_option.format(food)}").click()
        print(f"\nSelected food option {food}!")
        time.sleep(5)

    def container_displayed(self):
        print("Check if container is displayed")
        self.browser.find_element(*ExtraOptionsLocators.container)

    def close_extra_options(self):
        print("Closing the extra options container")
        self.browser.find_element(*ExtraOptionsLocators.close_button).click()

    def click_add_button(self):
        print("Clicking the add button")
        self.browser.find_element(*ExtraOptionsLocators.add_button).click()

    def get_alert_message(self):
        return self.browser.find_element(*ExtraOptionsLocators.alert_message).text

    def click_on_increase(self, no_of_times):
        n = 0
        while n < int(no_of_times):
            self.browser.find_element(*ExtraOptionsLocators.increase_button).click()
            n = n + 1

    def get_current_quantity(self):
        return self.browser.find_element(*ExtraOptionsLocators.quantity).text

    def get_current_price(self):
        return float(self.browser.find_element(*ExtraOptionsLocators.food_price).text.split(' ')[0])

    def click_on_decrease(self, no_of_times):
        n = 0
        while n < int(no_of_times):
            self.browser.find_element(*ExtraOptionsLocators.decrease_button).click()
            n = n + 1
        return int(self.get_current_quantity())
