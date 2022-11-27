from api_base.models import ModelBase
from ..models import Accounts
from django.db import models

class History_Action(ModelBase):
    account = models.ForeignKey(to=Accounts,on_delete=models.SET_NULL,default=None,blank=True,null=True,related_name="history_action")
    descriptions = models.CharField(max_length=999)

    class Meta:
        db_table = 'history_action'
