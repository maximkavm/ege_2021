a = [0]
for n in range(592121, 593011+1):
    deliteli=[]
    sq = int(n**0.5)
    for d in range(1, sq+1):
        if d*d == n:
            deliteli.append(sq)
        elif n % d == 0:
            deliteli.append(d)
            deliteli.append(n//d)
    if len(deliteli) > a[0]:
        a = [len(deliteli)]
        a.append(deliteli[-1])
        a.append(deliteli[-2])
print(a)

