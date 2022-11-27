import json
from datetime import datetime
from sys import path
import os
import django

path.append('C:/Users/gh/Desktop/Microservice/MicroService')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


from api_user.models import History_Action,Accounts


class Consumer_service:

    @classmethod
    def Login(cls, method, body):
        print(type(json.loads(body)))
        print('body:', json.loads(body), 'datetime:', datetime.now())

    @classmethod
    def history_action(cls,data:dict):
        account = Accounts.objects.filter(pk=data.get('account')).first()
        data['account'] = account
        histories = History_Action(**data)
        histories.save()
