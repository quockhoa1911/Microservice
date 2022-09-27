from rest_framework import serializers
from ..models import Roles

class Role_serializers(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields ='__all__'