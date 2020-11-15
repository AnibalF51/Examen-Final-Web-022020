from django import forms
from core.models import Equipos

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = "__all__"