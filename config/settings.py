import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # Browser config
    BROWSER = os.getenv("BROWSER", "chrome")

    # Headless = ejecutar sin ver el navegador (útil en CI/CD)
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"


    # URL del sitio a probar
    BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")

    # Testeo de credenciales
    TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL", "qa.automation@test.com")

    TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD", "TestPassword123!")


    # Wait Config
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))
