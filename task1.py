def prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n**5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(limit=None):
    num = 2
    while limit is None or num <= limit:
        if prime_number(num):
            yield num
        num +=1
