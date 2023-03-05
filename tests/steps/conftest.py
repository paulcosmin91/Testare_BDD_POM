import json
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

global driver
CONFIG_PATH = r"D:\IT curs\proiect final\Testare_BDD_POM_Restaurant_Bucovina\tests\config.json"


@pytest.fixture()
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture()
def setup(request, config):
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    if config["browser"] == "chrome":
        driver.maximize_window()
    yield
    driver.quit()


@pytest.fixture
def browser(config):
    if config["browser"] == "chrome":
        global driver
        options = Options()
        if config["headless_mode"] is True:
            options.add_argument("--headless")
        driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()
        return driver

    elif config["browser"] == "firefox":
        options = FirefoxOptions()
        if config["headless_mode"] is True:
            options.headless = True
        driver = selenium.webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
        return driver

    elif config["browser"] == "edge":
        options = EdgeOptions()
        if config["headless_mode"] is True:
            options.headless = True
        driver = selenium.webdriver.ChromiumEdge(service=Service(EdgeChromiumDriverManager().install()),
                                                 options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
        return driver
