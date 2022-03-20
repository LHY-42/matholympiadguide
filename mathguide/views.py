from django.shortcuts import render
from django.urls import reverse
from django.http import  HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.conf import settings
from django import forms
from django.forms import ModelForm, formset_factory, modelformset_factory

# Create your views here.
def index(request):


    return render(request, "mathguide/index.html")

