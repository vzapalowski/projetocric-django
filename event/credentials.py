from decouple import config

# Default to empty values so tests and non-email flows don't crash on import.
EMAIL = config('EMAIL_HOST_USER', default='')
PASSWORD = config('EMAIL_HOST_PASSWORD', default='')