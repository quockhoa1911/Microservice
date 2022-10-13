from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..serializer import MyTokenSerializers
from api_user.models import Accounts,Accounts_Roles
from django.contrib.auth.hashers import check_password,make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
jwt_authenticator = JWTAuthentication()
# Create your views here.


class LoginoutViews(ModelViewSet):
    serializer_class = MyTokenSerializers

    @action(methods=['POST'],detail=True,name='login')
    def login(self, request,pk=None,*args, **kwargs):
        serializer = self.serializer_class
        try:
            if pk is None:
                return Response(data="Invalid type role login",status=status.HTTP_400_BAD_REQUEST)
            username = request.data.get("username")
            password = request.data.get("password")
            account_role = Accounts_Roles.objects.filter(Q(account__username=username) & Q(role__name=pk.lower()) & Q(is_active=True))
            if account_role.exists():
                account_role = account_role.first()
                if not check_password(password,account_role.account.password):
                   return Response("is incorrect password",status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("data is not valid",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.get_token(account_role.account,account_role.role),status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, name='decode_token')
    def decode_token(self,request,*args,**kwargs):
        response = jwt_authenticator.authenticate(request=request)
        user , token = response
        print(token.payload)
        return Response(data="Ok",status=status.HTTP_200_OK)

