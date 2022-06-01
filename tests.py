import functools


def moves (h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


#@functools.lru_cache(maxsize=None)
@functools.lru_cache(maxsize=None)

def game(kucha):
    if sum(kucha) >= 231:
        return 'end'
    elif any(game(x) == 'end' for x in moves(kucha)):
        return 'p1'
    elif all(game(x) == 'p1' for x in moves(kucha)):
        return 'v1'
    elif any(game(x) == 'v1' for x in moves(kucha)):
        return 'p2'
    elif all(game(x) == 'p1' or game(x) == 'p2' for x in moves(kucha)):
        return 'v2'


for i in range(1, 99):
    h = (17, i)
    print(game(h), i)