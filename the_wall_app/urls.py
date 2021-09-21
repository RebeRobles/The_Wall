from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.wall),
    path('/new_message', views.new_message, name='new_message'),
    path('/new_comment', views.new_comment, name='new_comment'),
]