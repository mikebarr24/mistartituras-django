from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('buscar', views.buscar, name="buscar"),
    path('buscar/<str:inst>', views.instrument, name="instrument"),
    path('api', views.api, name="api"),
    path('part/<str:part_id>', views.part, name="part"),
    path('contacto', views.contacto, name="contacto"),
    path('login', views.login_view, name="login_view"),
    path('logout', views.logout_view, name="logout_view"),
    path('newuser', views.new_user, name="newuser"),
    path('account/<str:username>', views.account, name="account"),
]
