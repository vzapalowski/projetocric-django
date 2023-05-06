
from unidecode import unidecode

def replace(name):
    return unidecode(name).strip().lower().replace(' ', '_').replace('-', '_')