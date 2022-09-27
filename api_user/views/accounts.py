from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..models import Accounts
from ..serializer import Accounts_serializers
from ..services import Accounts_services
# Create your views here.

class Accountsviewset(ModelViewSet):
    serializer_class = Accounts_serializers
    queryset = Accounts.objects.all()

    def list(self, request, *args, **kwargs):
        queries = self.get_queryset()
        serializers = Accounts_serializers(many=True,data=queries)
        serializers.is_valid(raise_exception=False)
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=True,name='register_user_with_roles')
    def register_with_roles(self,request,pk,*args,**kwargs):
        return Accounts_services.register_with_roles(pk,request.data)







