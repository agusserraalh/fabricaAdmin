# prooccion/urls.py

from django.urls import path
from produccion import views

urlpatterns = [
    path("produccion", views.AddProduction.as_view(), name='produccion_add'),
    path("produccion/add", views.AddProduction.as_view(), name='produccion_add'),
    path("produccion/list", views.listProduccion.as_view(), name='produccion_list')
]