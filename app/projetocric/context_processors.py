from decouple import config

def env_vars(request):
    return {
        'ENVIRONMENT_URL': config('ENVIRONMENT_URL', default='http://127.0.0.1:8000'),
    }
