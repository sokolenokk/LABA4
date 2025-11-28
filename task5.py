def my_reduce(func, iterable, initial=None):
    iterator = iter(iterable)

    if initial is None:
        try:
            accumulator = next(iterator)
        except StopIteration:
            raise TypeError("my_reduce() для пустой итерации без начального значения")
    else:
        accumulator = initial

    for current in iterator:
        accumulator = func(accumulator, current)

    return accumulator


