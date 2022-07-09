from django.shortcuts import render
from .models import Instrument, Part
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
    return render(request, "parts/login.html")


def new_user(request):
    return render(request, "parts/new-user.html")
