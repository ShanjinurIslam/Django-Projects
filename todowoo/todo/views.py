from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def signupuser(request):
    if (request.method=='GET'):
        return render(request,'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        #create user

        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save() #saves it to database
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Username has already been taken'})

        else:
            # passwords didn't match
            return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Passwords didn\'t match'})

def loginuser(request):
    if (request.method=='GET'):
        return render(request,'todo/loginuser.html',{'form':AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password) ;
        if user is None:
            return render(request,'todo/loginuser.html',{'form':AuthenticationForm(),'error':'Username or Password didn\'t match'})
        else:
            login(request,user)
            return redirect('currenttodos')

def currenttodos(request):
    return render(request,'todo/current.html')

def landingpage(request):
    return render(request,'todo/landing.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landingpage')
