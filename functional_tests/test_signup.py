from .base import FunctionalTest
from functional_tests.pages.account_signup_window import AccountSignupWindow
from accounts.tests import util

class SignupTest(FunctionalTest):

    def test_signup_fails_with_repeated_user(self):
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