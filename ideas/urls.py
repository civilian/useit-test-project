from django.urls import path

from ideas.views import DeleteIdea, UpdateIdea

app_name = 'ideas'
urlpatterns = [
    path('delete/<int:pk>/', DeleteIdea.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateIdea.as_view(), name='update'),
]
