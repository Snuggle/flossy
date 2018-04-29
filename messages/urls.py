from django.urls import path
from . import views

urlpatterns = [
    # /messages/
    path('', views.index, name='index'),

    # /messages/Dave
    path('<str:contact>/', views.messageList, name='messageList'),
]
