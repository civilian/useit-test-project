from .base_page import BasePage
from functional_tests.base import wait

class AccountSignupWindow(BasePage):

    @wait
    def go_to_signup_page(self):
        self.go_to_home_page()
        self.test.browser.find_element_by_id('id_account_link').click()
        self.test.browser.find_element_by_id('id_signup_link').click()
        return self
    
    def write_in_username_input_box(self, text):
        self.write_in_any_input_by_id(text, 'id_username')
    
    def write_in_name_input_box(self, text):
        self.write_in_any_input_by_id(text, 'id_name')
    
    def write_in_lastname_input_box(self, text):
        self.write_in_any_input_by_id(text, 'id_lastname')
    
    def write_in_identification_number_input_box(self, text):
        self.write_in_any_input_by_id(text, 'id_identification_number')
    
    def write_in_password_input_box(self, text):
        self.write_in_any_input_by_id(text, 'id_password')
    
    def write_in_retype_password_input_box(self, text):
        self.write_in_any_input_by_id(text, 'id_retype_password')
    
    def click_signup_button(self):
        self.test.browser.find_element_by_css_selector('input[value="Signup"]').click()
    
    def create_user(self, profile):
        self.go_to_signup_page()
        self.write_in_username_input_box(profile.user.username)
        self.write_in_name_input_box(profile.user.first_name)
        self.write_in_lastname_input_box(profile.user.last_name)
        self.write_in_identification_number_input_box(profile.identification_number)
        self.write_in_password_input_box(profile.user.password)
        self.write_in_retype_password_input_box(profile.user.password)
        self.click_signup_button()
        self.check_message_in_messages('The user has been created')
        return self