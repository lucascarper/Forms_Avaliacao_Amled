from django import forms
from .models import Condutor

class CondutorForm(forms.ModelForm):
    class Meta:
        model = Condutor
        fields = ['foto', 'nome', 'cargo', 'equipamento', 'empresa', 'filial']
        widgets = {
            'nome': forms.TextInput(),
            'cargo': forms.TextInput(),
            'equipamento': forms.TextInput(),
            'empresa': forms.TextInput(),
            'filial': forms.TextInput(),
        }