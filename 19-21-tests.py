from functools import cache

def moves(heap):
    a, b = heap
    return (a + 1, b), (a, b + 1), (a * 4, b), (a, b * 4)
@cache
def game(heap):
    if sum(heap) >= 61:
        return 0
    steps = [game(x) for x in moves(heap)]
    if any(x % 2 == 0 for x in steps):
        return min(x for x in steps if x % 2 == 0) + 1
    else:
        return max(steps) + 1

for s in range(57, 0, -1):
    heap = (3, s)
    print(s, ": ", game(heap), " | ", [game(x) for x in moves(heap)])