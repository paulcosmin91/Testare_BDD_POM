from selenium.webdriver.common.by import By


class LogInLocators:
    URL = "https://www.restaurantbucovina.ro/Account/login"
    login_email_box = (By.XPATH, "//*[@id='LoginModel_Email']")
    login_password_box = (By.XPATH, "//*[@id='LoginModel_Password']")
    login_button = (By.XPATH, "//button[@id='btn-login']")
    email_error_message = (By.XPATH, "//em[@for='LoginModel_Email']")
    password_error_message = (By.XPATH, "//em[@for='LoginModel_Password']")
    login_error_message = (By.XPATH, "//div[contains(@class, 'sweet-alert')]/p")
    delivery_button = (By.XPATH, "(//button[contains(@class, 'btn-ship')])[1]")


class MainPageLocators:
    URL = "https://www.restaurantbucovina.ro/location"
    account_name = (By.XPATH, "//*[@id='welcome1']/a")
    logout_button = (By.XPATH, "//a[contains(@href,'logout')]")
    menu_button = "//div[@class='dropdown col-md-auto']/a[contains(text(),'{}')]"
