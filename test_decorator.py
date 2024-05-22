# 测试装饰器
# 1. 函数装饰器
import time

from functools import wraps


def count(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("waste time:", end_time-start_time)
    return wrapper


@count
def sum_total(num):
    total = 0
    for i in range(num):
        total += i
    return total


# 2. 类装饰器
class SumTotal:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func(*args, **kwargs)
        end_time = time.time()
        print("waste time:", end_time-start_time)


@SumTotal
def sum_total2(num):
    total = 0
    for i in range(num):
        total += i
    return total


sum_total2(100000)
