from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from datetime import date

# Create your views here.

# home page view


def home(request):
    return render(request, 'home.html')

# about page view


def about(request):
    return render(request, 'about.html')

# contact view


def contact(request):

    return render(request, 'contact.html')

# kisne kisne upload kiya


def uploaders(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = Signup.objects.all()

    d = {'users': user}

    return render(request, 'uploaders.html', d)


# user uploaded notes
def mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    # Order by the 'uploaddate' field in descending order
    notes = Notes.objects.filter(user=user).order_by('-uploaddate')
    d = {'notes': notes}

    return render(request, 'mynotes.html', d)

# to see pending status notes


def pendingnotes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="pending")
    d = {'notes': notes}

    return render(request, 'pending_notes.html', d)

# to see accepted status notes


def acceptednotes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="accept")
    d = {'notes': notes}

    return render(request, 'acceptednotes.html', d)

#  view for rejected notes


def rejectednotes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="reject")
    d = {'notes': notes}

    return render(request, 'rejectednotes.html', d)

# all notes ee to admin


def allnotes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.all()
    d = {'notes': notes}

    return render(request, 'allnotes.html', d)

# view all notes to user


def viewallnote(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    # Order by the 'uploaddate' field in descending order
    notes = Notes.objects.filter(status='accept').order_by('-uploaddate')
    d = {'notes': notes}
    return render(request, 'viewallnote.html', d)

#  uploader ko del krne k lie


def del_uploader(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('del_uploader')

#  user self uploaded notes  delete krne k lie


def del_notes(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('mynotes')


def del_all_notes(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('allnotes')

# view for assign status to notes


def assignstatus(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        # b = request.POST['nid']
        s = request.POST['ass']
        try:
            notes.status = s
            notes.save()
            error = 'no'
        except:
            error = 'yes'
    d = {
        'notes': notes, 'error': error
    }

    return render(request, 'assignstatus.html', d)

# view for user login


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

#  view for sign in


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

# view for user profile


def userprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data': data, 'user': user}

    return render(request, 'userprofile.html', d)

# view for logout


def Logout(request):
    logout(request)
    return redirect('home')

# view for admin homepage


def home_admin(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    pn = Notes.objects.filter(status='pending').count()
    ac = Notes.objects.filter(status='accept').count()
    rj = Notes.objects.filter(status='reject').count()
    al = Notes.objects.all().count()

    d = {'pn': pn, 'ac': ac, 'rj': rj, 'al': al}
    return render(request, 'homeadmin.html', d)

# admin login view


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

# notes upload logic


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
            Notes.objects.create(user=ct, uploaddate=date.today(),
                                 branch=b, subject=s, notes=n, filetype=f, description=d, status='pending')
            error = 'no'
            # Redirect to 'mynotes' page after successful upload
            return redirect('mynotes')
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, "notesupload.html", d)
