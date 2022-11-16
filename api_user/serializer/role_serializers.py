from rest_framework import serializers
from ..models import Roles

class Role_serializers(serializers.ModelSerializer):
    #if name field the same related name then no source else required source
    # status = serializers.SlugRelatedField(source="account_role",read_only=True,many=True,slug_field="is_active")
    # get one more fields use slug else get two or than  use Serializer model
    class Meta:
        model = Roles
        fields = ['id','name']
