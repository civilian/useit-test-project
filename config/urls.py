from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from boards.api import BoardViewSet
from ideas.api import IdeaViewSet
from boards.views import IndexPage

router = routers.DefaultRouter()
router.register(r'idea', IdeaViewSet)
router.register(r'board', BoardViewSet)

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('ideas/', include('ideas.urls')),
    path('api/', include(router.urls)),
]