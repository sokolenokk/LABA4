def read_clubs(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            yield line.strip()


def parse_club(line):
    parts = line.split(',')
    return {
        'название': parts[0],
        'страна': parts[1],
        'победы_лч': int(parts[2]),
        'год_основания': int(parts[3]),
        'стадион': parts[4]
    }


def filter_clubs(filename, country, min_wins):
    for line in read_clubs(filename):
        clubs = parse_club(line)
        if clubs['страна'] == country and clubs['победы_лч'] > min_wins:
            yield clubs


print("Испаниские клубы, у которых больше трех побед в Лиге Чемпионов")
print("-" * 62)

for club in filter_clubs('football_clubs.csv', country='Испания', min_wins=3):
    print(f"{club['название']}")
    print(f"Год основания: {club['год_основания']}")
    print(f"Стадион: {club['стадион']}")
    print(f"Побед в ЛЧ: {club['победы_лч']}")
    print('^' * 30)
