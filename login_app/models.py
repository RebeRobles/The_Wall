from django.db import models
from .models import *
import re

# Create your models here.
class UserManager(models.Manager):
    def fields_validator(self, postData):
        JUST_LETTERS = re.compile(r'^[a-zA-Z.]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])(?=\w*[0-9])\S{8,20}$')
        errors = {}

        if len(User.objects.filter(email = postData['email'])) > 0:
            errors['email_exists'] = 'Email ya registrado'
        else:
            if len(postData['first_name'].strip()) < 2 or len(postData['first_name'].strip()) > 100:
                errors['first_name_len'] = 'Nombre debe tener entre 2 y 100 caracteres'
            if len(postData['last_name'].strip()) < 2 or len(postData['last_name'].strip()) >100:
                errors['last_name_len'] ='Apeliido debe tener entre 2 y 100 caracteres'
            if not JUST_LETTERS.match(postData['first_name']) or not JUST_LETTERS.match(postData['last_name']):
                errors['just_letters'] = 'Nombre o apellido sólo se permite el ingreso de letras'
            if not EMAIL_REGEX.match(postData['email']):
                errors['email_format'] = 'Formato de correo electrónico no es válido'
            if not PASSWORD_REGEX.match(postData['password']):
                errors['password_format'] = 'Formato de contraseña no válido'
            if postData['password'] != postData['password_confirm']:
                errors['password_confirm'] ='Contraseñas no coinciden'
        return errors

            

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


    def __str__(self):
        return self.first_name +' '+ self.last_name

    def __repr__(self):
        return self.first_name +' '+ self.last_name

