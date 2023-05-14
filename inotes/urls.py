
from django.contrib import admin
from django.urls import path, include
from notes import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("notes.urls")),
]
