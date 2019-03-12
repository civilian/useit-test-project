from .base_page import BasePage
from functional_tests.base import wait

class AccountLoginWindow(BasePage):

    @wait
    def go_to_login_page(self):
        self.go_to_home_page()
        self.test.browser.find_element_by_id('id_account_link').click()
        self.test.browser.find_element_by_id('id_login_link').click()
        return self
    
    def click_login_button(self):
        self.test.browser.find_element_by_css_selector('input[value="Login"]').click()
 