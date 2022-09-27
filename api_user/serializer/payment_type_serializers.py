from rest_framework import serializers
from ..models import Payment_type
from ..serializer import Profile_Payment_type_serializers

class Payment_type_serializers(serializers.ModelSerializer):
    profile_payment_type = Profile_Payment_type_serializers(many=True)
    class Meta:
        model = Payment_type
        fields = ['id','payment_name','description','profile_payment_type']
