from django import forms
from event.models import Enrollment
from event.models.route_path import RoutePath


class EnrollmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route_path'].queryset = RoutePath.objects.filter(active=True)

    class Meta:
        model = Enrollment
        fields = '__all__'

    def clean_rg(self):
        rg = self.cleaned_data['rg']
        if Enrollment.objects.filter(rg=rg).exists():
            raise forms.ValidationError('RG já registrado')
        return rg
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Enrollment.objects.filter(email=email).exists():
            raise forms.ValidationError('EMAIL já existente')
        return email
