from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from boards.api import router

urlpatterns = [
    path('', TemplateView.as_view(template_name='boards/index.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('api/', include(router.urls)),
]