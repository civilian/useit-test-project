from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from boards.api import BoardViewSet
from ideas.api import IdeaViewSet

router = routers.DefaultRouter()
router.register(r'idea', IdeaViewSet)
router.register(r'board', BoardViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='boards/index.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('api/', include(router.urls)),
]