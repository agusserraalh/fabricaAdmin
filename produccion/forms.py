from django import forms
from .models import Production
from django.db import models

class ProductionForm(forms.ModelForm):

    class Meta:
        model = Production
        fields = ('id', 'cantidad')
        widgets = {
            'id': forms.HiddenInput(attrs={'id': 'edit_id'}),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_cantidad',
                'style': 'width: 100px; height: 30px; padding: 2px; font-size: 14px;',  # Estilos personalizados

            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['readonly'] = True
        self.fields['cantidad'].initial= 0
