from functools import wraps
from consumer_service import Consumer_service

scope_view = {
    'LoginadminUser':Consumer_service.Login,
    'LoginshopUser':Consumer_service.Login,
}

def consumer_decorator(func):
    @wraps(func)
    def inner(*args,**kwargs):
        method = args[1]
        routing_key = method.routing_key
        action_scope = scope_view.get(routing_key)
        if action_scope:
            action_scope(method,args[3])
        func(*args)
    return inner


