from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')


def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['upassword']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'

    d = {'error': error}

    return render(request, 'login.html')


def signin(request):

    return render(request, 'signin.html')


def userprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data': data, 'user': user}

    return render(request, 'userprofile.html', d)


def Logout(request):
    logout(request)
    return redirect('home')


def home_admin(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request, 'homeadmin.html')


def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['auser']
        p = request.POST['apass']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'

    d = {'error': error}
    return render(request, 'loginadmin.html', d)
