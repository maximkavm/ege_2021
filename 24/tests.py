file = open("tests.txt")

string = file.read()

max_cnt = 0
cnt = 1
for i in range(1, len(string)):
    if string[i] == 'B' and string[i - 1] == 'A' or string[i] == 'C' and string[i - 1] == 'A':
        cnt += 1
        max_cnt = max(max_cnt, cnt)
        i += 1
    else:
        cnt = 1

print(max_cnt)