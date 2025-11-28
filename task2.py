import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        spent_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнилась за {spent_time:.6f} сек")
        return result
    return wrapper


