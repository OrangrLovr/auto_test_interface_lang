from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_desription = ''

    def add_product_to_basket(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_desription()
        self.should_be_add_button()

        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()

        self.should_be_success()
        self.check_success_message()

    # return "The shellcoder's handbook"
    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # return "9,99 £"
    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # return "The Shellcoder's Handbook shows you how to: ..."
    def should_be_desription(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_desription = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    # check text 
    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Succes added product in " \
            "basket not found"

    # check button add
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'Add to basket' is not " \
            "presented"

    # check message
    def check_success_message(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(msg_lst) == 3, "Success message not found"

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"