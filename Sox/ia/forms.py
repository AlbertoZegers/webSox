from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        widgets = {'usuario': forms.HiddenInput()}