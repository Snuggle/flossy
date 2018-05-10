from django.contrib import admin
from .models import Contact, Message, Profile

# Register data models in admin panel
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Message)
