from appreview.models import AppVote
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import ProjectForm
from .models import AppVote

# Create your views here.
@login_required(login_url="/accounts/login")
def homepage(request):
    user=User.objects.get(id=request.user.id)
    apps=AppVote.objects.all()
    return render(request,'index.html',{"user":user,"apps":apps})
@login_required(login_url="/accounts/login")
def addproject(request):

    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.author=request.user.username
            project.save()
            redirect('index')
        print(form.errors)   
    form=ProjectForm()
    
    return render(request,"addproject.html",{"form":form})
def add(id):
    
    
    return redirect('index')
def logout(request):
    auth.logout(request)