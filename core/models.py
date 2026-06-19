from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='reports/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    scanned = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokens = models.IntegerField(default=0)

class Reward(models.Model):
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    image_filename = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
