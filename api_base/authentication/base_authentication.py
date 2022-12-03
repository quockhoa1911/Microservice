from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from api_base.constants import Base_Constant_Ignore_Token

class Base_Authentication(JWTAuthentication):
    def authenticate(self, request):
        check_continue = False
        header = request.META.get("HTTP_AUTHORIZATION",None)
        url = request.build_absolute_uri()
        for a in Base_Constant_Ignore_Token.values():
            if a in url:
                check_continue = True
        if not check_continue:
            if header is None:
                return None
                raise InvalidToken(("Token contained no recognizable user identification or Token not availalable"))
        return super().authenticate(request=request)
