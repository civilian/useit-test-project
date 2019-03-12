from faker import Faker
import factory
from django.contrib.auth import get_user_model

from accounts.models import Profile

def get_unsaved_user(*args, **kwargs):
    """Returns a user that has not been saved with the 
    password 'password' instead of a saved password that is long
    and comes with the salt"""
    profile = ProfileFactory.build(*args, **kwargs)
    profile.user.password = 'password'
    return profile

class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    user = factory.SubFactory('accounts.tests.util.UserFactory')
    identification_number = '2.234.988.234'

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = get_user_model()

    username = 'joe'
    first_name = 'joe'
    last_name = 'jhon'
    password = factory.PostGenerationMethodCall('set_password', 'password')

