a = []
for i in range(174457, 174505 + 1):
    deliteli = []
    sqr = int(i ** 0.5)
    for d in range(2, sqr + 1):
        if d * d == i:
            deliteli.append(d)
        if i % d == 0:
            deliteli.append(d)
            deliteli.append(i // d)
        if len(deliteli) > 2:
            break
    if len(deliteli) == 2:
        a.append(deliteli)
print(a)