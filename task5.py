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


clubs = [
    ("Реал Мадрид", 15),
    ("Милан", 7),
    ("Бавария", 6),
    ("Ливерпуль", 6),
    ("Барселона", 5),
    ("Аякс", 4),
    ("Интер", 3),
    ("Манчестер Юнайтед", 3),
]


best_club = my_reduce(
    lambda acc, club: acc if acc[1] > club[1] else club, clubs
)
print(f"Лучший клуб по титулам ЛЧ: {best_club[0]} ({best_club[1]} побед).")
print("Но лучший в мире все равно Барселона!")
