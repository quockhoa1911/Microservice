from django.db import models
from api_base.models import ModelBase
from ..models import Payment_type,Profiles


class Profiles_Payment_type(ModelBase):
    profile = models.ForeignKey(to=Profiles,on_delete=models.SET_NULL,related_name='profile_payment_type',blank=True,null=True,default=None)
    payment_type = models.ForeignKey(to=Payment_type,on_delete=models.SET_NULL,related_name='profile_payment_type',blank=True,null=True,default=None)
    payment_number = models.CharField(max_length=960,blank=True,null=True)

    class Meta:
        db_table = 'profiles_payment_type'
