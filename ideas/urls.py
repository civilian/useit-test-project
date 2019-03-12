from django.urls import path
from django.contrib.auth.decorators import login_required

from ideas.views import ( DeleteIdea, UpdateIdea, 
                           ConfirmAcceptIdea, accept_idea)

app_name = 'ideas'
urlpatterns = [
    path('delete/<int:pk>/', login_required(DeleteIdea.as_view()), name='delete'),
    path('update/<int:pk>/', login_required(UpdateIdea.as_view()), name='update'),
    path('confirm_accept/<int:pk>/', login_required(ConfirmAcceptIdea.as_view()), name='confirm_accept'),
    path('accept/<int:pk>/', login_required(accept_idea), name='accept'),
]
