from django.db import models
from django.contrib.auth.models import User
import hashlib

# This is the data model for a profile. It's one-to-one with Users and adds avatar images.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar_image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

# This is the data model for a contact. They link two Users together in a one-way direction.
class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown', unique=False, related_name='+')
    contact = models.ForeignKey(User, on_delete=models.CASCADE, default='Unknown', unique=False, related_name='+')
    # The '+' means that this will not have a backwards relation for this attribute.

    id = sorted([str(owner), str(contact)], key=str.lower)

    def __str__(self):
        return f'{self.owner} ➡️ {self.contact}' # This represents this object as a string.

# This is the data model for a message. It uses a contact as a ForeignKey and has a many->one relationship.
class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    message_text = models.CharField(max_length=1024)
    embed_image = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, related_name='+')

    def __str__(self):
        return str(hashlib.md5(str(self.message_text + str(self.contact)).encode('utf-8')).hexdigest())[:10]
        # This returns md5_hash(message_text + 'owner ⯈ contact') to allow easier retrieving of messages.
