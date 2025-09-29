from django import forms
from unidecode import unidecode

def replace(name):
    return unidecode(name).strip().lower().replace(' ', '_').replace('-', '_')

def validate_field(instance, model_class, field_name, error_message):
    field_value = instance.cleaned_data[field_name]

    if instance.instance.id is not None:
        return field_value

    if model_class.objects.filter(**{field_name: field_value}).exists():
        raise forms.ValidationError(error_message)

    return field_value