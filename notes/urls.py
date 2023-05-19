
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # link for users
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', userlogin, name='userlogin'),
    path('signin', signin, name='signin'),
    path('userprofile', userprofile, name='userprofile'),
    path('notesupload', notesupload, name='notesupload'),
    path('mynotes', mynotes, name='mynotes'),
    path('allnotes', allnotes, name='allnotes'),
    path('del_notes/<int:pid>', del_notes, name='del_notes'),
    path('del_all_notes/<int:pid>', del_all_notes, name='del_all_notes'),

    # links for admin
    path('logout', Logout, name='logout'),
    path('login_admin', login_admin, name='login_admin'),
    path('home_admin', home_admin, name='home_admin'),
    path('viewallnote', viewallnote, name='viewallnote'),
    path('pendingnotes', pendingnotes, name='pendingnotes'),
    path('acceptednotes', acceptednotes, name='acceptednotes'),
    path('rejectednotes', rejectednotes, name='rejectednotes'),
    path('uploaders', uploaders, name='uploaders'),
    path('assignstatus/<int:pid>', assignstatus, name='assignstatus'),
    path('del_uploader/<int:pid>', del_uploader, name='del_uploader'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
