f = open('24.txt')
s = f.readline()
cnt = 0
max_cnt = 0
for i in range(1, len(s)):
    if s[i] > s[i-1]:
        cnt += 1
        max_cnt = max(cnt, max_cnt)
    else:
        cnt = 1
print(max_cnt)