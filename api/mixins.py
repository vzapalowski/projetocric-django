from .utilities.auth_token import generate_auth_token

class ApiTokenMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth_token = generate_auth_token()
        self.request.session["auth_token"] = auth_token
        context["auth_token"] = auth_token
        return context
