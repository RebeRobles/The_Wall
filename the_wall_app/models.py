from django.contrib import messages
from login_app.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from .models import *

# Create your models here.

class MessageManager(models.Manager):
    def fields_validator(self, postData):
        errors = {}
        if len(postData['message'].strip()) < 2 or len(postData['message'].strip()) > 300:
            errors['message_len'] = 'Mensaje debe tener entre 2 y 300 letras'
        return errors

class CommentManager(models.Manager):
    def fields_validator(self, postData):
        errors = {}
        if len(postData['comment'].strip()) < 2 or len(postData['comment'].strip()) > 300:
            errors['comment_len'] = 'Coemntario debe tener entre 2 y 300 letras'
        return errors


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='message_user', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

    def __str__(self):
        return self.message

class Comment(models.Model):
    comment = models.TextField()
    messaage = models.ForeignKey(Message, related_name='comments', on_delete=CASCADE)
    uuser = models.ForeignKey(User, related_name='comment_user', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()