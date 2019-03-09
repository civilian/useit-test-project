from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification_number = models.CharField(max_lenght=100)
    image = models.ImageField(blank=True, null=True)
