from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets

from boards.models import Idea, Board

class IdeaSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        allow_blank=False, error_messages={'blank': "You can't have an empty list item"}
    )

    class Meta:
        model = Idea
        fields = ('id', 'board', 'text', 'accepted')

class BoardSerializer(serializers.ModelSerializer):
    ideas = IdeaSerializer(many=True, source='idea_set')

    class Meta:
        model = Board
        fields = ('id', 'private', 'ideas')

class IdeaViewSet(viewsets.ModelViewSet):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()

class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()



router = routers.DefaultRouter()
router.register(r'idea', IdeaViewSet)
router.register(r'board', BoardViewSet)