from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from boards import views as boards_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='boards/index.html')),
]