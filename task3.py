numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 77, 772, 770, 70, 0]

even_numbers_1 = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Четные через лямбду: {even_numbers_1}")

even_numbers_2 = [x for x in numbers if x % 2 == 0]
print(f"Четные через лист компрешн: {even_numbers_1}")
