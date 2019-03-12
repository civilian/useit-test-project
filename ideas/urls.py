from django.urls import path

from ideas.views import DeleteIdea

app_name = 'ideas'
urlpatterns = [
    path('delete/<int:pk>/', DeleteIdea.as_view(), name='delete'),
]
