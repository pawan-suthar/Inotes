from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    branch = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaddate = models.CharField(max_length=30, )
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=15)
    notes = models.FileField(null=True)
    filetype = models.CharField(max_length=30, )
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=10, )

    def __str__(self):
        return self.signup.user.username+""+self.status
