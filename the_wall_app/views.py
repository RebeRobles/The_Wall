from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def wall(request):
    context = {
        'messages': Message.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all().order_by('-created_at'),
    }
    return render(request,'the_wall_app/wall.html', context)
    
def new_message(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        if request.method == 'POST':
            errors = Message.objects.fields_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/wall')
            else:
                usuario = request.session['usuario']
                user = User.objects.get(id=usuario['id'])
                message = request.POST['message']
                obj_m = Message.objects.create(user=user, message=message)
                obj_m.save()
                return redirect('/wall')

def new_comment(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        if request.method == 'POST':
            errors = Comment.objects.fields_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/wall')
            else:
                usuario = request.session['usuario']
                user = User.objects.get(id=usuario['id'])
                msg = Message.objects.get(id=request.POST['message_id'])
                new_comment = request.POST['comment']
                obj_c = Comment.objects.create(uuser=user, messaage=msg, comment=new_comment)
                obj_c.save()
                return redirect('/wall')



