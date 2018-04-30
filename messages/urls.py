from django.urls import path, re_path
from . import views

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
    path('messages/<str:contact>/', views.messageList, name='messageList'),

    # /
    path('', views.index_view),

]
