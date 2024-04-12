from django import forms
from event.models import Enrollment3PasseioCiclistico, Bond
from event.models.route_path import RoutePath
from projetocric.utilities import validate_field

class enrollment3PasseioIfsulForm(forms.ModelForm):
    class Meta:
        model = Enrollment3PasseioCiclistico
        fields = ('full_name', 'date_of_birth', 'bond_choice', 'how_knew', 'rg', 'route', 'event', 'user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route_path'].queryset = RoutePath.objects.filter(active=True)
        self.fields['bond_choice'].queryset = Bond.objects.all()

    class Meta:
        model = Enrollment3PasseioCiclistico
        fields = '__all__'

    def clean_rg(self):
        return validate_field(self, Enrollment3PasseioCiclistico, 'rg', 'Este RG já foi cadastrado!')