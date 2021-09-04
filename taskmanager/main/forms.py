from .models import HiddenNumbers, guesswork, PowerOfAttorney
from django.forms import ModelForm, TextInput


class HiddenNumbersForm(ModelForm):
    class Meta:
        model = HiddenNumbers
        fields = ["numbers"]
        widgets = {"numbers": TextInput(attrs={
            'placeholder': 'загадонное число'
        })
        }


class guessworkForm(ModelForm):
    class Meta:
        model = guesswork
        fields = ["witch_1", "witch_2"]
