a = []
for n in range(160610, 160634+1):
    deliteli=[]
    sq = int(n**0.5)
    for d in range(2, sq+1):
        if n % d == 0:
            deliteli.append(d)
            deliteli.append(n//d)
        if len(deliteli) > 4:
            break
    if len(deliteli) == 4:
        deliteli.sort(reverse=True)
        print(deliteli)
        a.append(deliteli)
#print(a)