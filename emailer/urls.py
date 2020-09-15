from django.urls import path

from . import views

urlpatterns = [
    path('send-mail/', views.email, name='send-mail')
]
