a = []
for n in range(12000, 25000+1):
    deliteli=[1]
    sq = int(n**0.5)
    for d in range(2, sq+1):
        if d*d == n:
            deliteli.append(d)
        elif n % d == 0:
            deliteli.append(d)
            deliteli.append(n//d)
        if sum(deliteli) >= n:
            break
    if sum(deliteli) < n:
        a.append(n)
print(len(a))