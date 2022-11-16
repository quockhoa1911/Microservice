from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response

from api_user.models import Roles, Profiles, Accounts
from api_user.serializer import Role_serializers,Accounts_write_serializers
from django.db.models import Q


class Accounts_services:
    @classmethod
    def register_with_roles(cls,pk,data,*args,**kwargs):
        if pk is not None:
            role = Roles.objects.filter(name=pk)
            if not role.exists():
                return Response(data="Role not in database",status=status.HTTP_400_BAD_REQUEST)
            role = role.first()
            username = data.get("username",None)
            password = data.get("password",None)
            email = data.get("email",None)
            certificate = data.get('certificate',None)
            if username and password:
                if Accounts.objects.filter(username=username).exists():
                    return Response(data="username already in database", status=status.HTTP_400_BAD_REQUEST)
            if email and certificate:
               if Profiles.objects.filter(Q(email=email) | Q(certificate=certificate)).exists():
                   return Response(data="email or cerificate already in database",status=status.HTTP_400_BAD_REQUEST)

            data['roles'] = role.id.hex
            data['profile'] = {
                "email": email,
                "certificate":certificate
            }
            data.pop("email")
            data.pop("certificate")
            data['password'] = make_password(password)
            accountserializer = Accounts_write_serializers(data=data)
            if accountserializer.is_valid(raise_exception=True):
                accountserializer.save()
                return Response(data=accountserializer.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


