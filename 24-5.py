f = open('24.txt')
s = f.readline()
cnt = 0
for i in range(len(s) - 2):
    if s[i] in 'ACE' and s[i+1] in 'ADF' and s[i] != s[i+1] and s[i+2] in 'ABF' and s[i+1] != s[i+2]:
        cnt += 1
print(cnt)