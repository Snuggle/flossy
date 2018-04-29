from django.shortcuts import render
from django.http import Http404
from .models import Contact
from django.template import loader
from django.http import HttpResponse

def index(request):
    my_contacts = Contact.objects.all()
    return render(request, 'messages/index.html', {'my_contacts': my_contacts})

def messageList(request, contact):
    try:
        user = Contact.objects.get(id=contact)
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist.")
    return render(request, 'messages/user.html', {'user': user})
