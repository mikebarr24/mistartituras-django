import json
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect
from .models import Instrument, Part
from .forms import NewUserForm, LoginForm, PartForm
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


def part(request, part_id):
    part = Part.objects.get(pk=part_id)
    students = User.objects.filter(is_staff=False)
    return render(request, "parts/part.html", {
        "part": part,
        "students": students
    })


@csrf_exempt
def api(request):
    if request.method == "PUT" and data.get("type") == "add":
        data = json.loads(request.body)
        student_id = data.get("studentId")
        part_id = data.get("part")
        selected_part = Part.objects.get(pk=part_id)
        selected_student = User.objects.get(pk=student_id)
        selected_part.student.add(selected_student)
        return JsonResponse({
            "complete": f"{selected_part.part_title} has been added to {selected_student.username}"
        })
    elif request.method == "PUT" and data.get("type") == "remove":
        data = json.loads(request.body)
        part_id = data.get('part')
        selected_part = Part.objects.get(pk=part_id)
        selected_part.student.remove(request.user.id)
        return HttpResponse(200)
    elif request.method == "POST":

        return HttpResponse(200)


def contacto(request):
    return render(request, "parts/contacto.html")


def instrument(request, inst):
    selected_instrument = Part.objects.filter(instrument__instrument=inst)
    return render(request, "parts/instruments.html", {
        "parts": selected_instrument,
        'instrument': inst
    })


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("account", kwargs={"username": user}))
            else:
                logger.info("Not authorised to Access This Page")
    return render(request, "parts/login.html", {
        "form": LoginForm()
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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


@ login_required
@ csrf_exempt
def account(request, username):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            part_title = form.cleaned_data['part_title']
            composer_name = form.cleaned_data['composer_name']
            instrument = form.cleaned_data['instrument']
            level = form.cleaned_data['level']
            style = form.cleaned_data['style']
            curso = form.cleaned_data['curso']
            pdf = form.cleaned_data['pdf']
            audio = form.cleaned_data['audio']
            part = Part(part_title=part_title, composer_name=composer_name, instrument=instrument,
                        level=level, style=style, curso=curso, pdf=pdf, audio=audio)
            part.save()
            return HttpResponseRedirect(reverse("part", kwargs={"part_id": part.id}))

    student_parts = Part.objects.filter(student=request.user.id)
    return render(request, "parts/account.html", {
        "parts": student_parts,
        "form": PartForm
    })
