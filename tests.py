import itertools

for x in itertools.product("vasya", repeat=2):
    print("".join(x))
