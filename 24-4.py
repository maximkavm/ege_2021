f = open('24.txt')
s = f.readline()
cnt = 0
max_cnt = 0
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'B' or s[i] == 'C':
        cnt += 1
        max_cnt = max(cnt, max_cnt)
    else:
        cnt = 0
print(max_cnt)