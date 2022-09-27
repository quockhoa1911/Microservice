from django.db import models
from api_base.models import ModelBase
from ..models import Accounts

class Scopes(ModelBase):
    account = models.ForeignKey(to=Accounts,on_delete=models.CASCADE,related_name='scope',null=True,blank=True,default=None)
    scope_value = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'scopes'
