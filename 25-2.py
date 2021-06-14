a = []
for n in range(160610, 160634+1):
    deliteli=[]
    sq = int(n**0.5)
    if sq == n**0.5:
        continue
    for d in range(2, sq+1):
        if n % d == 0:
            if d % 2 == 0:
                deliteli.append(d)
            if (n // d) % 2 == 0:
                deliteli.append(n//d)
        if len(deliteli) > 4:
            break
    if len(deliteli) == 4:
        deliteli.sort(reverse=True)
        print(deliteli)
        a.append(deliteli)
#print(a)