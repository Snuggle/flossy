from django.db import models
from django.contrib.auth.models import User
import hashlib

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar_image = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown', unique=False, related_name='+')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown', unique=False, related_name='+')
    # The + means that this will not have a backwards relation for this attribute.

    id = sorted([str(owner), str(contact)], key=str.lower)

    def __str__(self):
        return f'{self.owner} ⯈ {self.contact}' # This represents this object as a string.

class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True, blank=True)
    message_text = models.CharField(max_length=1024)
    embed_image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(hashlib.md5(str(self.message_text + str(self.contact)).encode('utf-8')).hexdigest())[:10]
        # This returns md5(message_text + 'owner ⯈ contact')
