from rest_framework import serializers
from ..models import Profiles_Payment_type
from ..serializer import Payment_type_serializers

class Profile_Payment_type_serializers(serializers.ModelSerializer):
    payment_type = Payment_type_serializers(many=False,read_only=True)
    class Meta:
        model = Profiles_Payment_type
        fields = ['id','payment_number','payment_type']
