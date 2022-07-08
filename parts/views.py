from django.shortcuts import render


def index(request):
    return render(request, "parts/index.html")


def nosotros(request):
    return render(request, "parts/nosotros.html")


def buscar(request):
    return render(request, "parts/buscar.html")


def contacto(request):
    return render(request, "parts/contacto.html")
