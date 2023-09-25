from django import forms
from event.models import EnrollmentType2


class EnrollmentFormType2(forms.ModelForm):
    class Meta:
        model = EnrollmentType2
        fields = ('full_name', 'email', 'term_file')
