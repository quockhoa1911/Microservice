from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from api_user.models import Scopes
class MyTokenSerializers(serializers.Serializer):
    @classmethod
    def get_token(cls, account,role):
        token = RefreshToken.for_user(account)
        token['role_name'] = role.name
        scopes = Scopes.objects.filter(role=role.id.hex).first()
        if scopes is not None:
            token['scopes'] = scopes.scope_value
        return {
            "access_token" : str(token.access_token),
            "refresh_token" : str(token),
            "role" : str(role.name)
        }
