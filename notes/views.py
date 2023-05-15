from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from datetime import date

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')


def mynotes(request):

    return render(request, 'mynotes.html')


def userlogin(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['email']
        p = request.POST['upassword']
        user = authenticate(username=e, password=p)
        try:
            if user:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'

    d = {'error': error}

    return render(request, 'login.html', d)


def signin(request):
    error = ""
    if request.method == 'POST':
        # n = request.POST['uname']
        e = request.POST['uemail']
        # name and email user model me store
        c = request.POST['ucnumber']
        p = request.POST['upassword']
        b = request.POST['ubranch']
        # or baki ka signup model me
        try:
            user = User.objects.create_user(username=e, password=p)
            Signup.objects.create(user=user, contact=c, branch=b)
            error = 'no'
        except:
            error = 'yes'

    d = {'error': error}
    return render(request, 'signin.html', d)


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


def notesupload(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        b = request.POST['branch']
        ct = User.objects.filter(username=request.user.username).first()
        s = request.POST['subject']
        n = request.FILES['notes']
        f = request.POST['filetype']
        d = request.POST['description']

        try:
            Notes.objects.create(user=ct, uploaddate=date.today(
            ), branch=b, subject=s, notes=n, filetype=f, description=d, status='pending')
            error = 'no'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, "notesupload.html", d)
