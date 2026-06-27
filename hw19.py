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