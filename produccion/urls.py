# prooccion/urls.py

from django.urls import path
from produccion import views
from .views import sincronizar_productos

urlpatterns = [
    path("", views.AddProduction.as_view(), name='home'),
    path("produccion/", views.AddProduction.as_view(), name='produccion_add'),
    path("produccion/add/", views.AddProduction.as_view(), name='produccion_add'),
    path('produccion/editar/<uuid:uuid>/', views.produccion_edit, name='produccion_edit'),
    path('produccion/eliminar/<uuid:uuid>/', views.produccion_delete, name='produccion_delete'),
    path("produccion/list/", views.ListProduccion.as_view(), name='produccion_list'),
    path("produccion/sincronizarProductos/", sincronizar_productos, name='produccion_sincronizarProductos'),

]