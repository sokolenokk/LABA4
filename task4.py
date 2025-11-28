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
        'победы_лч': parts[2],
        'год_основания': parts[3],
        'стадион': parts[4]
    }
