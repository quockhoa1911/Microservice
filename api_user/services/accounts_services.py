from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response

from api_user.models import Roles, Profiles, Accounts
from api_user.serializer import Role_serializers,Accounts_write_serializers


class Accounts_services:
    @classmethod
    def register_with_roles(cls,pk,data,*args,**kwargs):
        if pk is not None:
            role = Roles.objects.filter(name=pk)
            if not role.exists():
                return Response(data="Role not in database",status=status.HTTP_400_BAD_REQUEST)

            role = role.first()
            username = data.get('username',None)
            profile = data.get('profile',None)
            email = profile.get('email',None)
            certificate = profile.get('certificate',None)
            # if email is not None:
            #     profile_queries = Profiles.objects.filter(email=email)
            #     if profile_queries.exists():
            #         account = Accounts.objects.filter(profile=profile_queries.first().id).exists()
            #         if account.count() > 1:
            #             for a in account:
            #                 if a.username == username:
            #                     return Response(data="Username and email is Already in data,"
            #                                      " if you forget account please authenticate accounts ",
            #                                     status=status.HTTP_400_BAD_REQUEST)
            #         else:
            #             if account.count() == 1:
            #                 if account.username == username:
            #                     return Response(data="Username and email is Already in data,"
            #                                          " if you forget account please authenticate accounts ",
            #                                     status=status.HTTP_400_BAD_REQUEST)
            #
            # if certificate is not None:
            #     if Profiles.objects.filter(certificate=certificate).exists():
            #         return Response(data="Certificate is already in data", status=status.HTTP_400_BAD_REQUEST)

            if Accounts.objects.filter(username=username).exists():
                return Response(data="username already in database",status=status.HTTP_400_BAD_REQUEST)

            data['role'] = role.id.hex
            accountserializer = Accounts_write_serializers(data=data)
            if accountserializer.is_valid(raise_exception=True):
                accountserializer.save()
                return Response(data=accountserializer.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


