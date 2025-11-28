def prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(limit=None):
    num = 2
    while limit is None or num <= limit:
        if prime_number(num):
            yield num
        num += 1


print("Первое 21 простое число:")
gen = prime_generator()
for _ in range(21):
    print(next(gen), end=" | ")
print()

print("\nВсе простые числа до 77:")
print(list(prime_generator(77)))
