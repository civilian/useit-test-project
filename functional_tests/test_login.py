from .base import FunctionalTest
from functional_tests.pages.account_signup_window import AccountSignupWindow
from functional_tests.pages.account_login_window import AccountLoginWindow
from accounts.tests import util

class LoginTest(FunctionalTest):

    def test_can_create_user_and_log_in(self):
        # Joe goes to the new boards app 
        # He sees an account link and clicks it
        
        # Then he clicks the signup link

        # He fills the username, the name, the lastname, 
        # the identification number, the password, and
        # Retypes the password

        # He clicks the signup now button

        # And the page tells him his user has been created
        profile = util.get_unsaved_user()
        AccountSignupWindow(self).create_user(profile)

        # Now he proceds to log in
        # He first goes to the index page and clicks the account link again

        # Now he goes to the login tab
        account_login_window = AccountLoginWindow(self).go_to_login_page()

        # And he introduces his username and his password
        account_login_window.write_in_username_input_box(profile.user.username)
        account_login_window.write_in_password_input_box(profile.user.password)

        # And he clicks the login button
        account_login_window.click_login_button()

        # Now he just logs out
        account_login_window.click_logout()