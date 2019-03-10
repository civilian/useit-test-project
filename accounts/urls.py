from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import SignUpPageView

app_name = 'accounts'
urlpatterns = [
    path('signup', SignUpPageView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]