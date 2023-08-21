from django import forms
from event.models import Enrollment, Bond
from event.models.route_path import RoutePath
from projetocric.utilities import validate_field


class EnrollmentForm(forms.ModelForm):
    # bond_choice = forms.ModelChoiceField(queryset=Bond.objects.all(), widget=forms.Select, required=True)

    class Meta:
        model = Enrollment
        fields = ('full_name', 'date_of_birth', 'bond_choice', 'how_knew', 'rg', 'route', 'event')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route_path'].queryset = RoutePath.objects.filter(active=True)
        self.fields['bond_choice'].queryset = Bond.objects.all()

    class Meta:
        model = Enrollment
        fields = '__all__'

    def clean_rg(self):
        return validate_field(self, Enrollment, 'rg', 'Este RG já foi cadastrado!')
    
    # def clean_email(self):
    #     return validate_field(self, Enrollment, 'email', 'EMAIL já cadastrado!')
