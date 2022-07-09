from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from .models import Instrument, Part
from .forms import NewUserForm, LoginForm
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "parts/index.html")


def nosotros(request):
    return render(request, "parts/nosotros.html")


def buscar(request):
    instruments = Instrument.objects.all()
    return render(request, "parts/buscar.html", {
        "instruments": instruments
    })


def contacto(request):
    return render(request, "parts/contacto.html")


def instrument(request, inst):
    selected_instrument = Part.objects.filter(instrument__instrument=inst)
    return render(request, "parts/instruments.html", {
        "parts": selected_instrument,
        'instrument': inst
    })


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            logger.info([username, password])
            user = authenticate(username=username, password=password)
            if user is not None:
                logger.info(user.email)
    return render(request, "parts/login.html", {
        "form": LoginForm()
    })


def new_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password_verify = form.cleaned_data["password_verify"]
            if password != password_verify:
                message = "Passwords do not match."
                return render(request, "parts/new-user.html", {
                    "message": message,
                    "form": NewUserForm()
                })
            user = User.objects.create_user(
                username=username, first_name=name, email=email, password=password)
            user.save()
            message = "You account has been created. Please go to the login page."
            return render(request, "parts/new-user.html", {
                "message": message,
                "form": NewUserForm()
            })
        else:
            return render(request, "parts/new-user.html", {
                "message": message,
                "form": NewUserForm()
            })
    return render(request, "parts/new-user.html", {
        "form": NewUserForm()
    })
