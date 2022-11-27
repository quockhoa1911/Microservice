from rest_framework.viewsets import ModelViewSet
from ..models import Payment_type
from ..serializer import Payment_type_serializers
from rest_framework.response import Response
from rest_framework import status
# Redis
from django.core.cache import cache
from django.conf import settings

class Paymentsviewset(ModelViewSet):
    queryset = Payment_type.objects.all()
    serializer_class = Payment_type_serializers
    scopes_view = {
        'list': 'admin:view,shop:view,user:view',
        'retrieve': 'admin:view,shop:view,user:view',
        'update': 'admin:update',
        'create': 'admin:create',
    }

    def list(self, request, *args, **kwargs):
        # if 'list_payment' in cache:
        #     print('get data in redis')
        #     return Response(data=cache.get('list_payment'), status=status.HTTP_200_OK)

        payments = self.get_queryset()
        serializers = self.get_serializer(instance=payments,many=True)
        # cache.set('list_payment',serializers.data)
        print('set data to redis')
        return Response(data=serializers.data,status=status.HTTP_200_OK)