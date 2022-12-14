from django.utils.module_loading import import_string
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from ..constants import Base_Constant_Ignore_Token
jwt_authenticator = JWTAuthentication()
class Base_Permission(BasePermission):

    def raw_decode_token(self,request):
        header = request.META.get("HTTP_AUTHORIZATION")
        if header is not None:
            header = header.encode('iso-8859-1')
            parts = header.split()
            token = parts[1]
            token_backend = import_string(
                "rest_framework_simplejwt.state.token_backend")
            payload = token_backend.decode(token, True)
            return payload
    def decode_token(self,request):
        response = jwt_authenticator.authenticate(request=request)
        user, token = response
        return token.payload

    def has_permission(self, request, view):
        try:
            if view.action in Base_Constant_Ignore_Token.values():
                return True

            scopes_view = view.scopes_view
            action_view = scopes_view.get(view.action, None)
            if action_view is None:
                return True

            scopes_token = request.auth.payload.get("scopes")
            list_scopes_token = scopes_token.split(",")
            list_scopes_action_view = action_view.split(",")
            for act in list_scopes_action_view:
                if act in list_scopes_token:
                    return True
            return False
        except:
            raise InvalidToken(("please authen before use this action"))


