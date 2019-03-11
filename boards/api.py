from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets

from boards.models import Idea, Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('id', 'private')

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ('id', 'board', 'text', 'accepted')

class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

class IdeaViewSet(viewsets.ModelViewSet):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()



router = routers.DefaultRouter()
router.register(r'idea', IdeaViewSet)
router.register(r'board', BoardViewSet)