from django.urls import path
from django.contrib.auth import views as auth_views

from boards.views import BoardsPageView, CreateBoardPageView

app_name = 'boards'
urlpatterns = [
    path('', BoardsPageView.as_view(), name='boards'),
    path('create_board', CreateBoardPageView.as_view(), name='create_board'),
]