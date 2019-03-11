from rest_framework import serializers, viewsets

from ideas.api import IdeaSerializer
from boards.models import Board



class BoardSerializer(serializers.ModelSerializer):
    ideas = IdeaSerializer(many=True, source='idea_set')

    class Meta:
        model = Board
        fields = ('id', 'private', 'ideas')



class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()