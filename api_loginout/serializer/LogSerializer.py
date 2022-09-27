from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from api_user.models import Scopes
class MyTokenSerializers(serializers.Serializer):
    @classmethod
    def get_token(cls, account):
        token = RefreshToken.for_user(account)
        token['role_name'] = account.role.name
        scope = Scopes.objects.filter(account=account)
        if scope is not None:
            token['scope'] = {scope.scope_value}
        return {
            "access_token" : str(token.access_token),
            "refresh_token" : str(token)
        }
