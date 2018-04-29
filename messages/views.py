from django.shortcuts import render, redirect
from django.http import Http404
from .models import Contact
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

def index_view(request):
    return render(request, 'messages/index.html', None)

def contacts(request):
    my_contacts = Contact.objects.all()
    return render(request, 'messages/contacts.html', {'my_contacts': my_contacts})

def messageList(request, contact):
    try:
        user = Contact.objects.get(id=contact)
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist.")
    messages = user.message_set.all()
    return render(request, 'messages/user.html', {'user': user, 'messages': messages})

def Logout(request):
    logout(request)
    return redirect('/')

class UserForm(View):
    form_class = UserForm
    template_name = 'messages/registration_form.html'

    # Display blank registration form
    def get (self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process data from form
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are valid
            user = authenticate(username=username, password=password)

            if user is not None: # Check user exists
                if user.is_active: # Check user is "active"

                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form': form})
