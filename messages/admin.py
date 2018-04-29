from django.contrib import admin
from .models import Contact, Message, Profile

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Message)
