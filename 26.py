f = open('26.txt')
n, k = map(int, f.readline().split())
znach = []
for s in f:
    znach.append(int(s))
znach.sort(reverse=True)
n_znach = znach[k:n-k]
print(max(n_znach), sum(n_znach) / len(n_znach))
