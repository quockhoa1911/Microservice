import json
from datetime import datetime

class Consumer_service():

    @classmethod
    def Login(cls,method,body):
        print(type(json.loads(body)))
        print('body:',json.loads(body),'datetime:',datetime.now())