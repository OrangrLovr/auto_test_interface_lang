from .base_page import BasePage
from .locators import ProductCheckInShoppingCartPageLocators

class BasketPage(BasePage):
    empty_basket_message = ''

    def should_be_see_product_in_basket_opened_from_main_page(self):
        self.should_be_btn_shopping_cart()

        btn_shopping_cart = self.browser.find_element(*ProductCheckInShoppingCartPageLocators.BTN_GO_TO_THE_SHOPPING_CART)
        btn_shopping_cart.click()

        self.should_be_empty_shopping_cart()
        self.should_be_succes_empty_text()
        self.check_succes_empty_message()

    # checking the presence of the "view basket" button
    def should_be_btn_shopping_cart(self):
        assert self.is_element_present(*ProductCheckInShoppingCartPageLocators.BTN_GO_TO_THE_SHOPPING_CART), "Button basket not found"

    # checking the availability of goods in the basket
    def should_be_empty_shopping_cart(self):
        assert self.is_not_element_present(*ProductCheckInShoppingCartPageLocators.BUSKET_ITEMS_IN_THE_SHOPPING_CART), "There are products in the basket"

    # checking the empty basket test
    def should_be_succes_empty_text(self):
        assert self.is_element_present(*ProductCheckInShoppingCartPageLocators.SUCCESS_EMPTY_BASKET_MESSAGES), "Empty basket message not found"
        self.empty_basket_message = self.browser.find_element(*ProductCheckInShoppingCartPageLocators.SUCCESS_EMPTY_BASKET_MESSAGES).text

    # checking two text values of an empty bucket
    def check_succes_empty_message(self):
        msg = self.browser.find_element(*ProductCheckInShoppingCartPageLocators.SUCCESS_EMPTY_BASKET_MESSAGES)

        assert self.empty_basket_message, "Wrong empty message №1"
        assert msg.text, "Wrong empty message №2"

        assert self.empty_basket_message == msg.text, "The first and second values are not equal"
