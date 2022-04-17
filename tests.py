import functools 

def moves(kucha):
    return kucha * 2, kucha + 1

@functools.lru_cache(maxsize=None)

def game(kucha):
    if kucha >= 29:
        return 'end'
    elif any(game(x) == 'end' for x in moves(kucha)):
        return 'P1'

#print(x for x in moves(kucha))