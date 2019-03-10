from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]