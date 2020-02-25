from django import forms
from .models import Producto

class ProduForm(foms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio']
        
