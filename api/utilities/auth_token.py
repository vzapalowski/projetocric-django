import secrets

def generate_auth_token():
    token = secrets.token_urlsafe(32)
    return token