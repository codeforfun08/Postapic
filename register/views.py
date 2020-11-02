from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    if(request.method=='POST'):
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        if(User.objects.filter(username=username).exists()):
            return render(request,"registration.html",{'message':"Username already taken"})
        elif(User.objects.filter(email=email).exists()):
            return render(request,"registration.html",{'message':"Someone already registered with this Email id"})
        else:
            user=User.objects.create_user(username=username,password=password,first_name=name,email=email)
            return render(request,"index.html") 
    else:
        
        return render(request,"index.html")
def register(request):
    return render(request,"registration.html")

def home(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password) 
        if(user is not None):
            auth.login(request,user)
            return redirect('homepage:postapic')
        else:
            return render(request,"index.html",{'message':"Username or password is incorrect"})
