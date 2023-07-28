import os
from django.core.exceptions import ValidationError


def files_list():
    files_list = {
        'category': ['.svg'],
        'city': ['.png, .jpeg'],
    }
    return files_list

def validate_file_extension_category(file):
    ext = os.path.splitext(file.name)[1]
    valid_extensions = files_list()['category']

    if not ext.lower() in valid_extensions:
        raise ValidationError("Tipo de arquivo não suportado")
