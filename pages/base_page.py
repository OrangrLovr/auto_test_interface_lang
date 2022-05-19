from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from math import sin, log
from .locators import BasePageLocatores

class BasePage():
    # timeout=10 
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # реализация неявного ожидания = 10 сек
        #self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # Проверка - элемент появляется на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Проверка - элемент не появляется на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Проверка - какой-то элемент исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # подсчет результата математического выражения
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocatores.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocatores.LOGIN_LINK)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocatores.USER_ICON), "User icon is not presented," \
            "probably unauthorised user"
