from django.db import models
import datetime
from django.utils.translation import gettext as _
from django import forms

class anotation(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(_("Date"), default=datetime.date.today)
    isfavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    email = models.EmailField()
    date = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return self.username
