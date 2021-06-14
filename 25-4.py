a = [999999999999999]
for n in range(416739, 418640+1):
    deliteli=[]
    sq = int(n**0.5)
    if sq == n**0.5:
        continue
    for d in range(1, sq+1):
        if n % d == 0:
            deliteli.append(d)
            deliteli.append(n//d)
        if len(deliteli) > 4:
            break
    if len(deliteli) == 4 and sum(deliteli) < a[0]:
        a = [sum(deliteli), 4, deliteli]
print(a)