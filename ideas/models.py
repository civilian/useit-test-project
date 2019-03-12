from django.db import models

from boards.models import Board

class Idea(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    text = models.TextField()
    accepted = models.BooleanField()

    def __str__(self):
        return self.text