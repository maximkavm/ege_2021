import functools

def moves (h):
    a, b = h
    return (a + 2, b), (a, b + 2), (a * 2, b), (a, b * 2)

@functools.lru_cache(maxsize=None)

def f(h):
    if (sum(h) >= 79):
        return 'end'
    elif (any(f(x) == 'end' for x in moves(h))):
        return 'P1'
    elif (all(f(x) == 'P1' for x in moves(h))): #for 19th use any
        return 'V1'
    elif (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    elif (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'

for i in range (1,100):
    h = 9, i
    print (i, f(h))