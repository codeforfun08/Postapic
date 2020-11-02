from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from homepage.models import post

@login_required(login_url="/")
def postapic(request):
    p=post.objects.all()
    np=p[::-1]
    return render(request,"test.html",{'posts':np})

@login_required(login_url="/")
def create(request):
    if(request.method=='POST'):
        desc=request.POST['desc']
        pic=request.FILES["pic"]
        pst=post.objects.create(uname=request.user,image=pic,desc=desc)
        pst.save()
        return redirect("homepage:postapic")
    else:
        return render(request,"create.html")

def logout(request):
    auth.logout(request)
    return redirect('register:index')

@login_required(login_url="/")
def profile(request):
    pst=post.objects.filter(uname=request.user)
    return render(request,"profile.html ",{"posts":pst})