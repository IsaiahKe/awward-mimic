from rest_framework import status
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import ProjectForm, UserForm,ProfileForm,ProjectVote
from .models import AppVote
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AppVoteApi
from .permissions import IsAdminOrReadOnly


# Create your views here.
@login_required(login_url="/accounts/login")
def homepage(request):
    user=User.objects.get(id=request.user.id)
    apps=AppVote.objects.order_by('total')[:4]
    sod=AppVote.objects.order_by('total')[0]
   
    title="Homepage"
    return render(request,'index.html',{"user":user,"apps":apps,"sod":sod,"title":title})
@login_required(login_url="/accounts/login")
def addproject(request):

    if request.method=="POST":
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.author=request.user.username
            project.save()
            return redirect('index')  
    form=ProjectForm()
    title="Add project"
    return render(request,"addproject.html",{"form":form,"title":title})
@login_required(login_url="/accounts/login/")
def profile(request,id):
    user=User.objects.get(pk=id)
    apps=AppVote.objects.filter(author=request.user.username)
    return render(request,"profile.html",{"user":user,"apps":apps})
@login_required(login_url="/accounts/login/")
def updateprofile(request,id):
    if request.method=="POST":
    
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES)
        print(userform.errors)
        print(profileform.errors)
        if userform.is_valid():
            userform.save(commit=False)
            userform.save()
        if profileform.is_valid():
            profileform.save(commit=False)
            profile.username_id=id
            profileform.save()
        
            return redirect('index')
    userform=UserForm()
    profileform=ProfileForm()
    title="Profile Update"
    return render(request,'update.html',{"userform":userform,"profileform":profileform,"title":title})
def add(request,id):
    errors=''
    if request.method=="POST":
        
        app=AppVote.objects.get(pk=id)
        form=ProjectVote(request.POST)
        #print(request.POST.get('usability'))
        def getv(res):#5.33333
            s=str(res)
            n=[]
            for i in s:
                n.append(i)
                if len(n)==3:
                    m=''.join(n)
                    return str(m)
        usability=str((float(request.POST.get('usability'))+float(app.usability))/2)
        design=str((float(request.POST.get('design'))+float(app.design))/2)
        content=str((float(request.POST.get('content'))+float(app.content))/2)
        res=getv(str((float(usability)+float(content)+float(design))/3))
        
        if form.is_valid():
            errors=''
            AppVote.objects.filter(id=id).update(usability=usability,design=design,content=content,total=getv(res))
            return redirect('index')
    vote=ProjectVote()
    title="App Vote"
    return render(request,'vote.html',{"form":vote,"errors":errors,"title":title})
def logout(request):
    auth.logout(request)
    return redirect('index')
def projects(request):
    apps=AppVote.objects.all()
    title="Projects View"
    return render(request,'projects.html',{"apps":apps,"title":title})
    
    
    #Api views
class AppList(APIView):
    
    def get(self,request,format=None):
        getAll=AppVote.objects.all()
        serializers=AppVoteApi(getAll,many=True)
        return Response(serializers.data)
    def post(self,request,format=None):
        permission_class=IsAdminOrReadOnly
        serializers=AppVoteApi(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)