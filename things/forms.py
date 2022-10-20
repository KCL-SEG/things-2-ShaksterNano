"""Forms of the project."""
from django.forms import ModelForm, Textarea, NumberInput, Widget

from things.models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ["name", "description", "quantity"]
        widgets = {"description": Textarea(), "quantity": NumberInput()}
