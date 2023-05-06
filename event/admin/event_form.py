from django import forms

from event.models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'routes': forms.CheckboxSelectMultiple,
        }