file = open("tests.txt")
s = file.readlines()
lst = [int(i) for i in s]
min_lst = min(lst)
cnt = 0
print(min_lst)
for i in range(len(lst)):
    if i == min_lst:
        cnt += 1

print(cnt)