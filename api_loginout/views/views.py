from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..serializer import MyTokenSerializers
from api_user.models import Accounts
from django.contrib.auth.hashers import check_password,make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
jwt_authenticator = JWTAuthentication()
# Create your views here.


class LoginoutViews(ModelViewSet):
    serializer_class = MyTokenSerializers

    @action(methods=['POST'], detail=False,name='login')
    def login(self, request, *args, **kwargs):
        serializer = self.serializer_class
        try:
            account = Accounts.objects.filter(username=request.data.get("username"))
            if account.exists():
                account = account.first()
                if not check_password(request.data.get('password'),account.password):
                   return Response("is incorrect password",status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("data is not valid",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.get_token(account),status=status.HTTP_200_OK)
    @action(methods=['GET'], detail=False, name='decode_token')
    def decode_token(self,request,*args,**kwargs):
        response = jwt_authenticator.authenticate(request=request)
        user , token = response
        print(token.payload)
        return Response(data="Ok",status=status.HTTP_200_OK)

