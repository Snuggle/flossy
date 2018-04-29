from django.db import models
from django.contrib.auth.models import User
import hashlib

class Contact(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default='Unknown', related_name='+')
    contact = models.OneToOneField(User, on_delete=models.CASCADE, default='Unknown', related_name='+')
    # The + means that this will not have a backwards relation for this attribute.

    def __str__(self):
        return f'{self.owner} ⯈ {self.contact}' # This represents this object as a string.

class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=1024)
    embed_image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return hashlib.md5(str(self.message_text + str(self.contact)).encode('utf-8')).hexdigest()
        # This returns md5(message_text + 'owner ⯈ contact')
