import pytest
from pages.home_page import HomePage
from utils.logger import get_logger

logger = get_logger(__name__)


class TestHomePageSmoke:


    @pytest.mark.smoke
    @pytest.mark.critical
    def test_home_page_loads(self, driver):


        logger.info("=" * 80)
        logger.info("TEST: Verificar que página principal carga")
        logger.info("=" * 80)


        home = HomePage(driver)


        home.navigate()


        assert "Automation Exercise" in driver.title, \
            f"Título incorrecto. Esperado: 'Automation Exercise', Actual: '{driver.title}'"


        assert home.is_element_visible(home.LOGO), \
            "El logo no es visible"


        current_url = home.get_current_url()
        assert "automationexercise" in current_url, \
            f"URL incorrecta: {current_url}"

        logger.info("✓ TEST PASÓ: La página se cargó correctamente")



    @pytest.mark.smoke
    def test_navigate_to_products(self, driver):


        logger.info("=" * 80)
        logger.info("TEST: Navegar a Productos")
        logger.info("=" * 80)


        home = HomePage(driver)
        home.navigate()


        home.click_products()


        home.wait_for_url_contains("/products")


        assert "/products" in driver.current_url, \
            f"No navegó a productos. URL actual: {driver.current_url}"

        logger.info("✓ TEST PASÓ: Navegación a Productos funcionó")



    @pytest.mark.smoke
    def test_login_link_visible(self, driver):


        logger.info("=" * 80)
        logger.info("TEST: Login link visible")
        logger.info("=" * 80)


        home = HomePage(driver)
        home.navigate()


        is_visible = home.is_element_visible(home.SIGNUP_LOGIN_LINK)

        assert is_visible, \
            "El link de Signup/Login no es visible"

        logger.info("✓ TEST PASÓ: Login link es visible")