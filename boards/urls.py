from django.urls import path
from django.contrib.auth import views as auth_views

from boards.views import ( ShowBoardsPageView, CreateBoardPageView, 
                           CrudIdeasPageView )

app_name = 'boards'
urlpatterns = [
    path('', ShowBoardsPageView.as_view(), name='boards'),
    path('create_board', CreateBoardPageView.as_view(), name='create_board'),
    path('crud_user_ideas/<int:board_pk>/', CrudIdeasPageView.as_view(), name='crud_user_ideas'),
]