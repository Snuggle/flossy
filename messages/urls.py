from django.urls import path, re_path
from . import views

# This file registers all the URL patterns that can be processed.
# Comments have been added to visuailise what they're matching.

urlpatterns = [

    # /settings
    path('settings/', views.settings, name='settings'),

    # /add_contact
    path('add_contact/', views.AddContactForm.as_view(), name='add_contact'),

    # /messages/
    path('messages/', views.contacts, name='contacts'),

    # /logout
    path('logout/', views.Logout, name='logout'),

    # /register
    path('register/', views.RegisterForm.as_view(), name='register'),

    # /register
    path('login/', views.LoginForm.as_view(), name='login'),

    # /messages/Dave
    path('messages/<str:contact>/', views.SendMessageForm.as_view(), name='SendMessageView'),

    # /
    path('', views.index_view),

]
