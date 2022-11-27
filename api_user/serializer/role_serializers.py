from rest_framework import serializers
from ..models import Roles

class Role_serializers(serializers.ModelSerializer):
    #if name field the same related name then no source else required source
    # status = serializers.SlugRelatedField(source="account_role",read_only=True,many=True,slug_field="is_active")
    # get one fields use slug else get two or more than  use Serializer model
    class Meta:
        model = Roles
        fields = ['id','name']
