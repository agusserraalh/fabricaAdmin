from django import forms
from .models import Production
from django.db import models

class ProductionForm(forms.ModelForm):

    class Meta:
        model = Production
        fields = ('id', 'cantidad')
        widgets = {
            'id': forms.HiddenInput(),  # Esto lo marca como oculto
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer el campo 'id' no editable 
        self.fields['id'].widget.attrs['readonly'] = True
        self.fields['cantidad'].initial= 0
