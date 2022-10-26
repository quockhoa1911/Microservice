

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from ..models import Accounts,Profiles
from ..serializer import Accounts_serializers,Profile_write_serializers
from ..services import Accounts_services
from api_base.permission import Base_Permission
# Create your views here.

class Accountsviewset(ModelViewSet):
    serializer_class = Accounts_serializers
    queryset = Accounts.objects.all().order_by("create_at")
    permission_classes = [Base_Permission]
    scopes_view = {
        "list":"user:view,shop:view,admin:view",
        "update_profile":"admin:update,user:update",
        "get_detail_user":"admin:view,user:view,shop:view"
    }
    def list(self, request, *args, **kwargs):
        queries = self.get_queryset()
        serializers = Accounts_serializers(many=True,instance=queries)
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=True,name='get_detail_user')
    def get_detail_user(self,request,pk,*args,**kwargs):
        user_instance = Accounts.objects.filter(pk=pk).first()
        serializer = Accounts_serializers(instance=user_instance,many=False)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True,name='register_with_roles')
    def register_with_roles(self,request,pk,*args,**kwargs):
        return Accounts_services.register_with_roles(pk,request.data)

    @action(methods=['PUT'],detail=False,name='update_profile')
    def update_profile(self,request,*args,**kwargs):
        data = request.data
        profile = Profiles.objects.filter(pk=data.get('id')).first()
        if request.auth.payload.get('role_name') != 'admin':

            if request.user.id.hex != profile.account.all().first().id.hex:
                return Response(data='update profile err',status=status.HTTP_400_BAD_REQUEST)

        profile_serializer = Profile_write_serializers(data=data,instance=profile)
        if profile_serializer.is_valid(raise_exception=True):
            profile_serializer.save()
        return Response(data='update success',status=status.HTTP_200_OK)







