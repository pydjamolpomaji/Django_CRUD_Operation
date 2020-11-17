from django.db import models


class User(models.Model):
    Name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=50)
