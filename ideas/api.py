from rest_framework import serializers, viewsets

from ideas.models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        allow_blank=False, error_messages={'blank': "You can't have an empty list item"}
    )

    class Meta:
        model = Idea
        fields = ('id', 'board', 'text', 'accepted')

class IdeaViewSet(viewsets.ModelViewSet):
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()