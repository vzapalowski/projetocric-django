from django import forms
from event.models import Enrollment, Bond



class EnrollmentForm(forms.ModelForm):
    bond_choice = forms.ModelChoiceField(queryset=Bond.objects.all())

    class Meta:
        model = Enrollment
        fields = ('full_name', 'date_of_birth', 'bond_choice', 'how_knew', 'rg', 'route')

    def clean_rg(self):
        rg = self.cleaned_data['rg']
        if Enrollment.objects.filter(rg=rg).exists():
            raise forms.ValidationError('RG already registered.')
        return rg