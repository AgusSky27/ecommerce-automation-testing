from selenium.webdriver.common.by import By


class HomePageLocators:

    SEARCH_BUTTON = (By.ID, "search-button")

    SEARCH_INPUT = (By.CSS_SELECTOR, ".search-field")

    PRODUCTS_LINK = (By.LINK_TEXT, "Products")

    CART_BADGE = (By.XPATH, "//span[@class='cart-count']")


class LoginPageLocators:

    EMAIL_INPUT = (By.NAME, "email")

    PASSWORD_INPUT = (By.NAME, "password")

    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Mensaje de error (si el login falla)
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")


class ProductPageLocators:

    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-item")

    PRODUCT_NAME = (By.CLASS_NAME, "product-name")

    PRODUCT_PRICE = (By.CLASS_NAME, "product-price")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[class*='add-to-cart']")


class CheckoutPageLocators:

    FIRST_NAME_INPUT = (By.NAME, "first_name")

    LAST_NAME_INPUT = (By.NAME, "last_name")

    ADDRESS_INPUT = (By.NAME, "address")

    CONFIRM_PURCHASE_BUTTON = (By.ID, "confirm-order")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")