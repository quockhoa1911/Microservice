from django.db import models
from api_base.models import ModelBase
from ..models import Accounts

class Accounts_infor(ModelBase):
    avatar = models.CharField(max_length=950,null=True,blank=True)
    account = models.ForeignKey(to=Accounts,on_delete=models.SET_NULL,blank=True,null=True,related_name='account_infor',default=None)

    class Meta:
        db_table = 'accounts_infor'

