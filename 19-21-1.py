import functools

def moves(a):
    return a + 1, a * 2


@functools.lru_cache(maxsize=None)
def f(h):
    if h >= 65:
        return 'end'
    elif any(f(x) == 'end' for x in moves(h)):
        return 'p1'
    elif all(f(x) == 'p1' for x in moves(h)): # for 19th use any
        return 'v1'
    elif any(f(x) == 'v1' for x in moves(h)):
        return 'p2'
    elif all(f(x) == 'p1' or f(x) == 'p2' for x in moves(h)):
        return 'v2'

for s in range(1, 100):
    print(s, f(s))
