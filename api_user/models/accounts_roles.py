from django.db import models
from api_base.models import ModelBase
from ..models import Accounts
from ..models import Roles

class Accounts_Roles(ModelBase):
    account = models.ForeignKey(to=Accounts,on_delete=models.SET_NULL,blank=True,null=True,default=None,related_name='account_role')
    role = models.ForeignKey(to=Roles,on_delete=models.SET_NULL,blank=True,null=True,default=None,related_name='account_role')
    class Meta:
        db_table = 'accounts_roles'