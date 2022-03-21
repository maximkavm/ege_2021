f = open('24.txt')
s = f.readline()
d = dict()
for i in range(1, len(s)):
    if s[i-1] == 'A':
        d[s[i]] = d.get(s[i], 0) + 1;
print(d)