from django import forms
from event.models import Event
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'points': forms.CheckboxSelectMultiple,
            'routes_data': forms.CheckboxSelectMultiple,
            'warnings': forms.CheckboxSelectMultiple,
        }
        
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
