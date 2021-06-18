f = open('27-6b.txt')
n = int(f.readline())
m = 0
m2 = 0
m3 = 0
m6 = 0
for i in range(n):
    x = int(f.readline())
    if x % 6 == 0 and x > m6:
        if m6 > m:
            m = m6
        m6 = x
    elif x > m:
        m = x
    if m % 2 == 0 and x % 6 != 0 and x > m2:
        m2 = x 
    if m % 3 == 0 and x % 6 != 0 and x > m3:
        m3 = x
print(max(m2*m3, m6*m))