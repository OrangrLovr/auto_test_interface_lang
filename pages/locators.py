from sre_constants import SUCCESS
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".product_main form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

class BasePageLocatores():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class ProductCheckInShoppingCartPageLocators():
    BTN_GO_TO_THE_SHOPPING_CART = (By.CSS_SELECTOR, ".basket-mini span a.btn-default")
    BUSKET_ITEMS_IN_THE_SHOPPING_CART = (By.CSS_SELECTOR, ".basket-items.row")
    SUCCESS_EMPTY_BASKET_MESSAGES = (By.CSS_SELECTOR, "#content_inner p")
