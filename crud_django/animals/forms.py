from dataclasses import fields
from django.forms import ModelForm
from .models import Animals
class AnimalForm(ModelForm):
    class Meta():
        model= Animals
        fields='__all__'