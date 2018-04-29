from django.db import models

class User(models.Model):
    username = models.CharField(max_length=16)
    avatar_image = models.CharField(max_length=100)

    def __str__(self):
        return self.username # This represents this object as a string.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=1024)
    embed_image = models.CharField(max_length=100)
