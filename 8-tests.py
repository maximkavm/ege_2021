import itertools

count = 0
for x in itertools.product("ШКОЛА", repeat=3):
    if "".join(x).count('К') == 1:
        count += 1

print(count)