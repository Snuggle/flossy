from django.shortcuts import render, redirect
from django.http import Http404
from .models import Contact, Message
from django.template import loader
from django.http import HttpResponse
from itertools import chain
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, AddContactForm, SendMessageForm

def index_view(request):
    return render(request, 'messages/index.html', None)

@login_required(login_url='/login/')
def contacts(request):
    my_contacts = []
    logged_in_user = request.user
    all_contacts = Contact.objects.all()
    for contact in all_contacts:
        if contact.owner == logged_in_user:
            my_contacts.append(contact)
    return render(request, 'messages/contacts.html', {'my_contacts': my_contacts})

@login_required(login_url='/login/')
def settings(request):
    return render(request, 'messages/settings.html', None)

class AddContactForm(View):
    form_class = AddContactForm
    template_name = 'messages/add_contact.html'

    # Display blank login form
    def get (self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        contacts = Contact.objects.all()

        username = request.POST['username']
        user = User.objects.get(username=username)
        contact = Contact(owner=request.user, contact=user)
        contact.save()
        return redirect('/')

class SendMessageForm(View):
    form_class = SendMessageForm
    template_name = 'messages/user.html'

    def get(self, request, contact):
        error_message = None
        incomingContact = None
        messages = None
        incomingMessages = None
        try:
            contact = Contact.objects.get(id=contact)
        except Contact.DoesNotExist:
            raise Http404("Contact does not exist.")

        try:
            incomingContacts = Contact.objects.filter(owner=contact.contact)
            print(incomingContacts)
            incomingContact = incomingContacts.get(contact=contact.owner)
            print(incomingContact)
            if incomingContact is None:
                raise Exception.ValueError
            outgoingMessages = contact.message_set.all()
            incomingMessages = incomingContact.message_set.all()

            messages = list(chain(incomingMessages, outgoingMessages))

            messages = sorted(messages, key=lambda message: message.datetime)

        except DoesNotExist:
            print("User attempted to access a contact that hasn't added them back.")
            error_message = "This user hasn't added you back yet!"

        return render(request, 'messages/user.html', {'contact_context': contact, 'error_message': error_message, 'messages': messages})

    def post(self, request, contact):
        contactObject = Contact.objects.get(id=contact)
        message = request.POST['message']
        messageObject = Message(contact=contactObject, message_text=message, owner=contactObject.owner)
        messageObject.save()
        return redirect(f'/messages/{contactObject.id}')

def Logout(request):
    logout(request)
    return redirect('/')

class LoginForm(View):
    form_class = LoginForm
    template_name = 'messages/login_form.html'

    # Display blank login form
    def get (self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process data from form
    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        # returns User object if credentials are valid
        user = authenticate(request, username=username, password=password)

        if user is not None: # Check user exists
            if user.is_active: # Check user is "active"

                login(request, user)
                return redirect('/')

        return render(request, self.template_name, {'form': form})

class RegisterForm(View):
    form_class = RegisterForm
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
