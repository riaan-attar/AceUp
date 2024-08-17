from django import forms
from django.forms import inlineformset_factory
from user.models import *

class EventsForm(forms.ModelForm):
    class Meta:
        model = events
        fields = ['title', 'date', 'time', 'bd', 'description', 'thumbnail']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 80}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['photos', 'photoCaption', 'url']