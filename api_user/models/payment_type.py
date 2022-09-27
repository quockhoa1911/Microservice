from api_base.models import ModelBase
from django.db import models

class Payment_type(ModelBase):

    payment_name = models.CharField(max_length=960)
    description = models.TextField()

    class Meta:
        db_table = 'payment_type'



