from django.urls import path
from .views import *

urlpatterns = [
    path('producto/', Producto.as_view(),name='producto'),
]