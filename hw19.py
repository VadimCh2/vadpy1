from typing import Callable
from functools import wraps

def decorator_add_10(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if type(result) == int:
            result = result + 10
        return result
    return wrapper

@decorator_add_10
def add_numbers(number_1: int, number_2: int):
    return number_1 + number_2

@decorator_add_10
def divide_numbers(number_1: float, number_2: float):
    return number_1 / number_2

result_1 = add_numbers(5, 7)
print(result_1)
result_2 = divide_numbers(5, 2)
print(result_2)