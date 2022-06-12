from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login



# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
     if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        user1 = User.objects.create_user(username,email,psw)
        user1.save()
        messages.success(request,"Account created")
        return redirect('/login_user')

     return render(request,'register.html')

def login_user(request): 
    if request.method == 'POST':
       username = request.POST['username']
       psw = request.POST['psw']
       user = authenticate(username=username, psw=psw)
       if user is not None:
          login(request,user)
          return redirect('index')


       else:
           messages.error(request,"Error,try again")
           return render(request,'login_user.html')


    return render(request,'login_user.html')
    
        


