from django.db import models
from chat.models import CustomUser


class TokenUsage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tokens = models.IntegerField(default=0)
