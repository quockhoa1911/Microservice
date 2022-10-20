from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from api_base.constants import Base_Constant
class Base_Authentication(JWTAuthentication):

    def authenticate(self, request):
        header = request.META.get("HTTP_AUTHORIZATION")
        url = request.build_absolute_uri()
        if Base_Constant.get("checkurl",None) not in url:
            if header is None:
                raise InvalidToken(("Token contained no recognizable user identification or Token not availalable"))
        super().authenticate(request=request)
