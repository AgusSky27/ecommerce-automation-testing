from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import Settings
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:


    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, Settings.EXPLICIT_WAIT)

        self.logger = get_logger(self.__class__.__name__)



    def find_element(self, locator):

        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            self.logger.info(f"✓ Elemento encontrado: {locator}")

            return element

        except TimeoutException:
            self.logger.error(f"✗ Elemento NO encontrado: {locator}")

            self.take_screenshot(f"element_not_found")

            raise

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

        self.logger.info(f"✓ Click en: {locator}")



    def send_keys(self, locator, text):

        element = self.find_element(locator)

        element.clear()

        element.send_keys(text)

        if "password" in str(locator).lower():
            self.logger.info(f"✓ Texto escrito (password oculto): {locator}")
        else:
            self.logger.info(f"✓ Texto escrito en {locator}: {text}")



    def get_text(self, locator):

        element = self.find_element(locator)
        text = element.text

        self.logger.info(f"✓ Texto obtenido de {locator}: '{text}'")

        return text



    def is_element_visible(self, locator):

        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False



    def take_screenshot(self, name="screenshot"):

        import os
        from datetime import datetime

        os.makedirs("reports/screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/screenshots/{name}_{timestamp}.png"

        self.driver.save_screenshot(filename)

        self.logger.warning(f"📸 Screenshot guardado: {filename}")



    def get_current_url(self):

        return self.driver.current_url


    def wait_for_url_contains(self, url_fragment):

        self.wait.until(EC.url_contains(url_fragment))
        self.logger.info(f"✓ URL contiene: {url_fragment}")