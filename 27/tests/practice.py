from functools import lru_cache

#условие:
# >= 77 - проигрыш
# +1, *2


#главная идея: нечётное кол-во ходов до конца - выигрышная позиция, чётное - проигрышная позиция
#хотим перевести противника в проигрышную позицию, поэтому среди states ищем чётные
#если нашли выигрышные ходы, то берём самый короткий путь к победе, иначе берём самый длинный путь к поражению


def Moves(heaps):
    a = heaps
    return a + 1, a + 2, a * 2


@lru_cache(maxsize=None)
def Count(heaps): #считает кол-во ходов до конца игры при оптимальной игре обоих игроков
    if heaps >= 22:
        return 0
    states = [Count(move) for move in Moves(heaps)]
    wins = [state for state in states if not state % 2]
    if len(wins):
        return min(wins) + 1
    return max(states) + 1


for i in range(1, 22):
    print(i, Count(i))

