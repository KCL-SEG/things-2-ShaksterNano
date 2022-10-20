"""Forms of the project."""
from django.forms import ModelForm, Textarea, NumberInput, Widget

from things.models import Thing


class ThingForm(ModelForm):
    class Meta:
        model: Thing = Thing
        fields: list[str] = ["name", "description", "quantity"]
        widgets: dict[str, Widget] = {"description": Textarea(), "quantity": NumberInput()}
