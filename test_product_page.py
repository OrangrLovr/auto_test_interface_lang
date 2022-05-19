from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        register_page = LoginPage(browser, link)
        register_page.open()

        # действие по переходу к регистрации
        # проверка элементов регистрации
        # регистрация нового пользователя
        # проверка что пользователь залогинент
        register_page.should_be_register_new_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success()

    @pytest.mark.parametrize('link', [*range(1,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
    def test_user_can_add_product_to_basket(self, browser, link):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()

    # данную функцию прописали в setup
    """
    def test_user_can_register_new_user(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        login = LoginPage(browser, link)
        login.should_be_register_new_user()
    """

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(reason="the test will crash due to the wrong selector")
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_see_product_in_basket_opened_from_main_page()
