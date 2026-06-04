import pytest
from utils.driver_factory import DriverFactory
from utils.logger import get_logger

logger = get_logger("conftest")



@pytest.fixture(scope="function")
def driver():



    logger.info("=" * 80)
    logger.info("🚀 SETUP: Creando WebDriver")
    logger.info("=" * 80)

    driver = DriverFactory.get_driver()

    yield driver


    logger.info("=" * 80)
    logger.info("🛑 TEARDOWN: Cerrando WebDriver")
    logger.info("=" * 80)

    driver.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):


    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            from datetime import datetime
            import os

            test_name = item.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            os.makedirs("reports/screenshots", exist_ok=True)

            filename = f"reports/screenshots/FAILED_{test_name}_{timestamp}.png"

            driver.save_screenshot(filename)

            logger.error(f"❌ TEST FALLÓ - Screenshot: {filename}")



def pytest_configure():

    import os

    logger.info("📁 Creando directorios necesarios...")

    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/logs", exist_ok=True)

    logger.info("✓ Directorios listos")



def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador a usar: chrome o firefox"
    )


@pytest.fixture
def browser(request):

    return request.config.getoption("--browser")