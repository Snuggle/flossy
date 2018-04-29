from django.urls import path, re_path
from . import views

urlpatterns = [

    # /messages/
    path('messages/', views.contacts, name='contacts'),

    # /messages/logout
    path('logout/', views.Logout, name='logout'),

    # /messages/register
    path('register/', views.UserForm.as_view(), name='register'),

    # /messages/Dave
    path('messages/<str:contact>/', views.messageList, name='messageList'),

    # /
    path('', views.index_view),

]
