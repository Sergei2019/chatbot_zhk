from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page, name='chat'),
    path('api/', views.chat_api, name='chat_api'),
]