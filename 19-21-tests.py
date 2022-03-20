import functools

def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@functools.lru_cache(maxsize=None)

def f(h):
    if sum(h) >= 77: # end
        return 'end'
    elif (any(f(x) == 'end' for x in moves(h))):
        return 'P1'
    elif (any(f(x) == 'P1' for x in moves(h))): #for 19th use any
        return 'V1'
    elif (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    elif (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'

for s in range(1, 100):
    h = 7, s
    print(s, f(h))