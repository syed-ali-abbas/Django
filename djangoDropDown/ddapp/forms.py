from django import forms
from .models import City,Country, Person

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model=Person
        fields= ('country','city')


    