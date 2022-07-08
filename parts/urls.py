from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('buscar', views.buscar, name="buscar"),
    path('contacto', views.contacto, name="contacto"),
]
