from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Settings


class LoginPage(BasePage):



    SIGNUP_NAME_INPUT = (By.NAME, "name")

    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")

    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-btn']")


    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-btn']")



    ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")



    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Settings.BASE_URL}/login"

    def navigate(self):

        self.driver.get(self.url)
        self.logger.info(f"✓ Navegando a: {self.url}")



    def signup_user(self, name, email):

        self.logger.info(f"✓ Registrando usuario: {name} / {email}")

        self.send_keys(self.SIGNUP_NAME_INPUT, name)

        self.send_keys(self.SIGNUP_EMAIL_INPUT, email)

        self.click(self.SIGNUP_BUTTON)

        self.logger.info("✓ Formulario de signup enviado")


    def login_user(self, email, password):

        self.logger.info("✓ Intentando login...")

        self.send_keys(self.LOGIN_EMAIL_INPUT, email)

        self.send_keys(self.LOGIN_PASSWORD_INPUT, password)

        self.click(self.LOGIN_BUTTON)

        self.logger.info("✓ Formulario de login enviado")



    def is_error_message_displayed(self):

        return self.is_element_visible(self.ERROR_MESSAGE)

    def get_error_message(self):

        if self.is_error_message_displayed():
            return self.get_text(self.ERROR_MESSAGE)

        return None