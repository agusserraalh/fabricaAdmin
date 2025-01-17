# prooccion/urls.py

from django.urls import path
from produccion import views

urlpatterns = [
    path("", views.home, name='produccion'),
]