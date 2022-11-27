from rest_framework.viewsets import ModelViewSet
from ..models import Roles
from ..serializer import Role_serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
# Redis
from django.core.cache import cache
from django.conf import settings

CACHE_TTL = getattr(settings,'CACHE_TTL',12*60)

class Rolesviewset(ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = Role_serializers
    scopes_view = {
        'list': 'admin:view',
        'retrieve': 'admin:view,shop:view,user:view',
        'update': 'admin:update',
        'create': 'admin:create',
        'get_role_for_user': 'admin:view,shop:view,user:view'
    }

    def list(self, request, *args, **kwargs):
        if 'list_role' in cache:
            print('get data in redis')
            return Response(data=cache.get('list_role'), status=status.HTTP_200_OK)

        roles = self.get_queryset()
        serializers = self.get_serializer(instance=roles, many=True)
        print('set data to redis')
        cache.set('list_role', serializers.data,CACHE_TTL)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, name='get_role_for_user')
    def get_role_for_user(self, request, *arg, **kwargs):
        if 'get_role_for_user' in cache:
            print('get data in redis')
            return Response(data=cache.get('get_role_for_user'), status=status.HTTP_200_OK)
        roles = Roles.objects.filter(~Q(name__contains='admin'))
        serializers = Role_serializers(instance=roles, many=True)
        cache.set('get_role_for_user', serializers.data,CACHE_TTL)
        print('set data to redis')
        return Response(data=serializers.data, status=status.HTTP_200_OK)
