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


@timer
def slow_sum(n):
    answer = 0
    for i in range(1, n + 1):
        answer += i
    return answer


@timer
def fast_sum(n):
    return n * (n + 1) // 2


print("Результат подсчета медленной функции", slow_sum(7777777))
print()
print("Результат подсчета быстрой функции", fast_sum(7777777))
