from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField()
    title = models.CharField(max_length=100)


