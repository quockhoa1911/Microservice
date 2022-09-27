from rest_framework import serializers
from ..models import Profiles_Payment_type

class Profile_Payment_type_serializers(serializers.ModelSerializer):
    class Meta:
        model = Profiles_Payment_type
        fields = ['id','payment_number']
