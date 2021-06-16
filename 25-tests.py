a = []
sm = 0
for i in range(4986, 32599 + 1):
    deliteli = []
    sqr = int(i ** 0.5)
    for j in range(2, sqr + 1):
        if j * j == i:
            deliteli.append(j)
        elif i % j == 0:
            deliteli.append(j)
            deliteli.append(i // j)
        if len(deliteli) > 2:
            break
    if len(deliteli) == 2:
        sm += i
print(sm)