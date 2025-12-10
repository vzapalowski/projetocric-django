from rest_framework.permissions import BasePermission

class HasApiAuthToken(BasePermission):
    message = "Access denied: invalid or missing auth token"
    
    def has_permission(self, request, view):
        session_token = request.session.get("auth_token")
        header_token = request.headers.get("X-Auth-Token") or request.META.get("HTTP_X_AUTH_TOKEN")
        return bool(session_token and header_token and session_token == header_token)