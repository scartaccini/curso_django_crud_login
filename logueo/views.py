from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , authenticate , logout#login, crea una cookie (ssesionid)
from django.contrib.auth.models import User


def index(request):    
    return render(request, 'index.html')

##### LOGUEO, DESLOGUEO, CREACION DE USUARIO 
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)#crea una cookie (ssesionid)
                return redirect('index')
                #return render(request, 'index.html')
            except:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})
    
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('index')
    
def signout(request):
    logout(request)
    return redirect('index')

##### LOGUEO, DESLOGUEO, CREACION DE USUARIO 

