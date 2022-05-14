import functools

def moves(heap):
    return (heap + 1), (heap * 2)

@functools.lru_cache(maxsize=None)

def game(heap):
    if heap >= 223:
        return 'end'
    elif any(game(x) == 'end' for x in moves(heap)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    elif any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    elif all(game(x) in {'P1', 'P2'} for x in moves(heap)):
        return 'V2'

for s in range(1, 210):
    heap = s
    print(s, game(heap))
