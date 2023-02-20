from selenium.webdriver.common.by import By
from locators.locators import MainPageLocators


class MenuPage:
    def __init__(self, browser):
        self.browser = browser

    def get_account_name(self):
        return self.browser.find_element(*MainPageLocators.account_name).text

    def click_menu_buttons(self, button_name):
        button_list = ["KIMPOLUNG", "Recomandări", "Promoții Combo", "Mic Dejun", "Gustări", "Ciorbe",
                       "Salate Aperitiv", "Tradiționale", "Carne de Pui", "Carne de Porc", "Carne de Vită",
                       "Vegans & Post", "More..."]
        for i in range(len(button_list)):
            if button_list[i] == button_name:
                self.browser.find_element(By.XPATH, f"{MainPageLocators.menu_button.format(button_name)}").click()
                print("\nClick!")
