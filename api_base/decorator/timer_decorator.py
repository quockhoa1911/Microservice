from functools import wraps
from time import time


def timer_smart(func):
    # coppy func with func, name, parameter
    @wraps(func)
    def inner(*arg,**kwargs):
        time_before = time()
        func(*arg,**kwargs)
        time_after = time()
        print(f"Time line start function: {func.__name__}, before :{time_before}, after:{time_after}, sum:{time_after-time_before}")
    return inner


# @timer_smart #decorator time_smart nhan ham test la tham so, tu dong thao tac ben trong inner
# def test(name):
#     print(f"Hello {name}")
#
#
# test("AAA")
