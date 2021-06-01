f = open('24.txt')
s = f.readline()
cnt = 1
max_cnt = 1
for i in range(1, len(s)):
    if s[i:i+3] == 'XYZ':
        cnt += 3
        max_cnt = max(cnt, max_cnt)
    elif s[i:i+2] == 'XY':
        cnt += 2
        max_cnt = max(cnt, max_cnt)
        cnt = 0
    elif s[i:i+1] == 'X':
        cnt += 1
        max_cnt = max(cnt, max_cnt)
        cnt = 0
print(max_cnt)