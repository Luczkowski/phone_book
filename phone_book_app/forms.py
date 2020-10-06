from django.forms import ModelForm
from .models import Osoba, Telefon, Email

class OsobaForm(ModelForm):
    class Meta:
        model = Osoba
        fields = ['imie', 'nazwisko']

class TelefonForm(ModelForm):
    class Meta:
        model = Telefon
        fields = ['telefon']


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email']
