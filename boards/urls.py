from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from boards.views import ( ShowBoardsPage, CreateBoardPage, 
                           CrudIdeasPage )

app_name = 'boards'
urlpatterns = [
    path('', login_required(ShowBoardsPage.as_view()), name='boards'),
    path('create_board', login_required(CreateBoardPage.as_view()), name='create_board'),
    path('crud_user_ideas/<int:board_pk>/', login_required(CrudIdeasPage.as_view()), name='crud_user_ideas'),
]