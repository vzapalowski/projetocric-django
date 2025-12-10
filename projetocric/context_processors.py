from decouple import config
from django.conf import settings

def env_vars(request):
    return {
        'ENVIRONMENT_URL': config('ENVIRONMENT_URL', default='http://127.0.0.1:8000'),
        'FEATURE_EMAIL_ENABLED': settings.FEATURE_EMAIL_ENABLED,
    }
