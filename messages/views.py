from django.shortcuts import render
from .models import User
from django.template import loader
from django.http import HttpResponse

def index(request):
    all_users = User.objects.all()
    template = loader.get_template('messages/index.html')
    context = {
        'all_users': all_users,
    }
    return HttpResponse(template.render(context, request))

def messageList(request, contact):
    return HttpResponse("<h2>Messages for Contact: " + str(contact) + "</h2>")
