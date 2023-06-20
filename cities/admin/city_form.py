from django import forms
from cities.models import City


class CityAdminForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'routes': forms.CheckboxSelectMultiple,
            'points': forms.CheckboxSelectMultiple
        }
        