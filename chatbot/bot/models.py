from django.db import models

from django.contrib.auth.models import User

class Dialog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    text = models.TextField()
    is_bot = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
