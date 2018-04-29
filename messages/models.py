from django.db import models
from django.contrib.auth.models import User
import hashlib

class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown', related_name='+')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown', related_name='+')
    # The + means that this will not have a backwards relation for this atrribute.

    def __str__(self):
        return self.username # This represents this object as a string.

class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=1024)
    embed_image = models.CharField(max_length=100)

    def __str__(self):
        return hashlib.md5(contact.username + self.message_text)
