from .base_page import BasePage

class MainPage(BasePage):

    # можно использовать pass вместо init
    def __init__(self, *args, **kwargs):
        '''
        super вызывает конструктор класса предка и передает ему 
        все те аргументы, которые мы передали в конструктор MainPage.      
        '''
        super(MainPage, self).__init__(*args, **kwargs)


    '''
    Перенос данных функций в base_page.py

    # нахождение элемента с сылкой на предка
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # метод для нахождения логина элемента
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"'''

