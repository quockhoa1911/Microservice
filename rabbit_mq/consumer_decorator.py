import json
from functools import wraps
from consumer_service import Consumer_service
def consumer_decorator(func):
    @wraps(func)
    def inner(*args,**kwargs):
        method = args[1]
        body = args[3]
        routing_key = method.routing_key
        print(routing_key)
        if routing_key == 'login':
            Consumer_service.history_action(data=json.loads(body))
        func(*args)
    return inner


