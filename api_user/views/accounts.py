from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
import json
from api_base.pagination import Base_CustomPagination
from api_base.permission import Base_Permission


from ..models import Accounts,Profiles,Accounts_Roles,Roles
from ..serializer import Accounts_serializers,Profile_write_serializers
from ..services import Accounts_services
from django.db.models import Q

from rabbit_mq import publish


# Create your views here.

class Accountsviewset(ModelViewSet):
    serializer_class = Accounts_serializers
    queryset = Accounts.objects.all().order_by("create_at")
    # pagination_class = Base_CustomPagination
    # permission_classes = [Base_Permission]
    scopes_view = {
        "list":"shop:view,admin:view",
        "update_profile":"admin:update,shop:update,user:update",
        "retrieve":"admin:view,shop:view,user:view",
        "get_user":"admin:view,shop:view,user:view",
        "register_another_role":"shop:update,user:update",
        "up_image":"admin:create,shop:create,user:create",
        "get_list_shop":None
    }
    def list(self, request, *args, **kwargs):
        queries = self.get_queryset()
        page = self.paginate_queryset(queries)
        if page:
            serializers = Accounts_serializers(instance=page,many=True)
            return self.get_paginated_response(data=serializers.data)
        serializers = Accounts_serializers(many=True,instance=queries)
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self, request,pk=None, *args, **kwargs):
        user_instance = Accounts.objects.filter(pk=pk).first()
        serializer = Accounts_serializers(instance=user_instance, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False,name='get_user',url_path='me/get_user')
    def get_user(self,request,*args,**kwargs):
        pk = request.user.id.hex
        user_instance = Accounts.objects.filter(pk=pk).first()
        serializers = Accounts_serializers(instance=user_instance,many=False)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True,name='register_with_roles')
    def register_with_roles(self,request,pk,*args,**kwargs):
        return Accounts_services.register_with_roles(pk,request.data)

    @action(methods=['POST'],detail=False,name='up_image',url_path='me/up_image')
    def up_image(self,request,*args,**kwargs):
        file = request.FILES.get('files')
        if file:
            pk = request.user.id.hex
            profile = Profiles.objects.filter(account__id=pk).first()
            file_url = Accounts_services.upload_file(file)
            profile.avatar = file_url
            profile.save()
            return Response(data=file_url,status=status.HTTP_200_OK)
        return Response(data='file is not valid',status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PUT'],detail=False,name='update_profile',url_path='me/update_profile')
    def update_profile(self,request,*args,**kwargs):
        pk = request.user.id.hex
        data = request.data
        # fe convert form data to object json before send data to be
        profile = Profiles.objects.filter(account=pk).first()
        profile_serializer = Profile_write_serializers(data=data,instance=profile)
        if profile_serializer.is_valid(raise_exception=True):
            profile_serializer.save()
        return Response(data='update success',status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=True,name='register_another_role')
    def register_another_role(self,request,pk,*args,**kwargs):
        id_user = request.user.id.hex
        account_role = Accounts_Roles.objects.filter(Q(account=id_user) & Q(role__name=pk))
        if account_role.exists():
            return Response(data='account already role',status=status.HTTP_400_BAD_REQUEST)
        else:
            account = Accounts.objects.get(pk=id_user)
            role = Roles.objects.filter(name__icontains=pk).first()
            acc = Accounts_Roles(account=account,role=role)
            acc.save()
            account = acc.account
            accountserializers = Accounts_serializers(instance=account)
            publish(method='register', body=json.dumps(
                {
                    'message': json.dumps(accountserializers.data)
                }), routing_key='Register' + pk.title() + 'Event')
            return Response(data='register success',status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False,name='get_list_shop')
    def get_list_shop(self,request,*args,**kwargs):
        account = Accounts.objects.filter(Q(account_role__is_active=True) & Q(account_role__role__name='shop'))
        if account.exists():
            page = self.paginate_queryset(account)
            serializers = Accounts_serializers(instance=page,many=True)
            return Response(data=serializers.data,status=status.HTTP_200_OK)
        return Response(data='No shop in data',status=status.HTTP_400_BAD_REQUEST)







