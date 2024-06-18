# myapp/forms.py
from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['type', 'gender', 'birth_date', 'tag_number']

class RemoveAnimalForm(forms.Form):
    REMOVAL_REASON_CHOICES = (
        ('sold', 'Sold'),
        ('death', 'Death'),
    )
    removal_reason = forms.ChoiceField(choices=REMOVAL_REASON_CHOICES, required=True)
