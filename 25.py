def f(a, b) :
    for i in range(a, b):
        k = 1
        d = 0
        res = []
        while k*k < i + 1:
            if i % k == 0:
                if k != i//k:
                    d += 2
                    res.extend([k, i//k])
                else :
                    d += 1
            if d > 4 :
                break
            k += 1
        if d == 4:
            print(*sorted(res)[-2:])

f(251811, 251826 + 1)