from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

#registrar usuarios
def signup(request):
    if request.method == 'GET':
        return render(request,"signup.html",{
        'from':UserCreationForm
        })
    else:
        # print("ya pues")
        # print(request.POST['password1'])
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('view_project')

            except IntegrityError:
                return render(request,"signup.html",{
                            'from':UserCreationForm,
                            'error':'el usuario ya existe'
                            })
        else:
            return render(request,"signup.html",{
                            'from':UserCreationForm,
                            'error':'la contraseña o coincide'
                            })


#iniciar sesion
def signin(request):
    if request.method=='GET':
        return render(request,'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user= authenticate(request,username=request.POST['username'],password=request.POST['password'])#cauntetificando el usuario
        if user is None:
            return render(request,'signin.html',{
                'form':AuthenticationForm,
                'error':'el user o password es incorrecto'
            })
        else:
            login(request,user)
            return redirect("view_project")

#cerrar sesion
@login_required
def signout(request):
    logout(request)
    return redirect('home')
