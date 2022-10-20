from rest_framework import serializers
from ..models import Payment_type

class Payment_type_serializers(serializers.ModelSerializer):

    # profile_payment_type_detail = Profile_Payment_type_serializers(many=True,read_only=True,source="profile_payment_type")
    # profile_payment_type_detail = serializers.SlugRelatedField(many=True,read_only=True,slug_field="payment_number")
    # if name field the same related name then no source else required source
    # get one more fields use slug else get two or than  use Serializer model
    class Meta:
        model = Payment_type
        fields = ['id','payment_name','description']
