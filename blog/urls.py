from django.urls import path
from . import wiews

urlpatterns = [
    path('', views.post_list, name='post_list'),
]