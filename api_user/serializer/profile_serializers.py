from rest_framework import serializers
from ..models import Profiles,Profiles_Payment_type,Payment_type
from ..serializer import Profile_Payment_type_serializers

class Profile_serializers(serializers.ModelSerializer):
    profile_payment_type = Profile_Payment_type_serializers(many=True,read_only=True)
    class Meta:
        model = Profiles
        fields = ['id','name','gender','age','phone_number','email','certificate','avatar','profile_payment_type','province',
                  'province_code','ward','ward_code','district','district_code','address']

class Profile_write_serializers(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ['id','name','gender','age','phone_number','avatar','province',
                  'province_code','ward','ward_code','district','district_code','address']
    def to_internal_value(self, data):
        global profile_payment_type
        if data.get("profile_payment_type",None):
            profile_payment_type = data.pop("profile_payment_type")
        return super().to_internal_value(data)

    def update(self, instance, validated_data):
        prf_u = super().update(instance=instance,validated_data=validated_data)
        list_update_payment = []
        list_create_payment = []

        for i in profile_payment_type:
            id = i.get('id',None)
            payment_number = i.get('payment_number')
            if id:
               pr_pm_ty = Profiles_Payment_type.objects.filter(pk=id).first()
               pr_pm_ty.payment_number = payment_number
               list_update_payment.append(pr_pm_ty)
            else:
                id_pm = i.get('payment_type').get('id')
                pm_ty = Payment_type.objects.filter(pk=id_pm).first()
                inst = Profiles_Payment_type(profile=prf_u,payment_type=pm_ty,payment_number=payment_number)
                list_create_payment.append(inst)

        Profiles_Payment_type.objects.bulk_update(list_update_payment,fields=['payment_number'])
        Profiles_Payment_type.objects.bulk_create(list_create_payment)
        return prf_u

