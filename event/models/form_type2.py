from django import forms
from event.models import EnrollmentType2


class EnrollmentFormType2(forms.ModelForm):
    class Meta:
        model = EnrollmentType2
        fields = ('full_name', 'email', 'term_file')
        widgets = {
            'term_file': forms.ClearableFileInput(attrs={'accept': '.pdf, .jpeg, .jpg, .png'}),
        }

    class Meta:
        model = EnrollmentType2
        fields = '__all__'
