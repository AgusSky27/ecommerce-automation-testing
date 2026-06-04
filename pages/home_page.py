from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Settings


class HomePage(BasePage):

    LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")

    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")

    SIGNUP_LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")

    CART_LINK = (By.LINK_TEXT, "Cart")

    LOGGED_IN_AS = (By.XPATH, "//*[contains(text(), 'Logged in as')]")

    LOGOUT_LINK = (By.LINK_TEXT, "Logout")


    def __init__(self, driver):

        super().__init__(driver)

        self.url = Settings.BASE_URL


    def navigate(self):

        self.driver.get(self.url)

        self.wait_for_page_load()

        self.logger.info(f"✓ Navegando a: {self.url}")

    def wait_for_page_load(self):

        self.find_element(self.LOGO)
        self.logger.info("✓ Página principal cargada")



    def click_products(self):

        self.click(self.PRODUCTS_LINK)
        self.logger.info("✓ Click en: Products")

    def click_signup_login(self):

        self.click(self.SIGNUP_LOGIN_LINK)
        self.logger.info("✓ Click en: Signup / Login")

    def click_cart(self):

        self.click(self.CART_LINK)
        self.logger.info("✓ Click en: Cart")

    def click_logout(self):

        if self.is_logged_in():
            self.click(self.LOGOUT_LINK)
            self.logger.info("✓ Logout realizado")
        else:
            self.logger.warning("⚠ No estás logueado, logout no disponible")



    def is_logged_in(self):

        is_logged = self.is_element_visible(self.LOGGED_IN_AS)

        if is_logged:
            self.logger.info("✓ Usuario logueado")
        else:
            self.logger.info("✗ Usuario NO logueado")

        return is_logged

    def get_logged_username(self):

        if self.is_logged_in():
            text = self.get_text(self.LOGGED_IN_AS)

            username = text.replace("Logged in as ", "").strip()

            self.logger.info(f"✓ Usuario actual: {username}")

            return username

        return None