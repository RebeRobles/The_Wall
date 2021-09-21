from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def home(request):
    return render(request, 'login_app/login.html')

def register(request):
    if request.method =='GET':
        return redirect('/')
    else:
        if request.method == 'POST':
            errors = User.objects.fields_validator(request.POST)

            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)

                request.session['registro_nombre'] = request.POST['first_name']
                request.session['registro_apellido'] = request.POST['last_name']
                request.session['registro_email'] = request.POST['email']
            else:
                request.session['registro_nombre'] = ''
                request.session['registro_apellido'] =''
                request.session['registro_email'] = ''

                nombre = request.POST['first_name']
                apellido = request.POST['last_name']
                email = request.POST['email']
                password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

                obj = User.objects.create(first_name=nombre, last_name=apellido, email=email, password=password_hash)
                obj.save()
                messages.success(request, 'Usuario registrado con éxito')
            return redirect ('/')
        return render(request, 'login_app/login.html')

def login(request):
    if request.method == 'GET':
        return redirect('login_app/login.html')
    else:
        if request.method == 'POST':
            user = User.objects.filter(email = request.POST['email_login'])
            if len(user) > 0:
                usuario_registrado = user[0]
                if bcrypt.checkpw(request.POST['password_login'].encode(), usuario_registrado.password.encode()): 
                    usuario = {
                        'id' : usuario_registrado.id,
                        'nombre': usuario_registrado.first_name,
                        'apellido': usuario_registrado.last_name,
                        'email': usuario_registrado.email,
                    }

                    request.session['usuario'] = usuario
                    messages.success(request, 'Ingreso correcto')
                    return redirect('/wall')
                else:
                    messages.error(request, 'Datos erróneos o el usuario no existe')
                    return redirect('login_app/login.html')
            else:
                messages.error(request, 'Datos mal ingresados o el usuario no existe')
                return redirect('/')
        
def logout(request):
    request.session.flush()
    return redirect('/')


