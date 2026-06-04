from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import Settings


class DriverFactory:

    @staticmethod
    def get_driver():

        chrome_options = ChromeOptions()

        # Útil para CI/CD o tests rápidos
        if Settings.HEADLESS:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")

        prefs = {"profile.default_content_setting_values.notifications": 2}


        chrome_options.add_experimental_option("prefs", prefs)

        service = ChromeService(ChromeDriverManager().install())

        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )


        driver.implicitly_wait(Settings.IMPLICIT_WAIT)

        driver.set_page_load_timeout(20)

        if not Settings.HEADLESS:
            driver.maximize_window()

        return driver