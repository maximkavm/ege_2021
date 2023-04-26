# 162

file = open('tests.txt')
a = [0] * 150
count = 0

for s in file.readlines():
    count += 1
    k = 1
    if count == 162:
        for i in range(len(s)):
            a[ord(s[i])] = a[ord(s[i])] + 1


char = ''
mx = 0
for i in range(150):
    if a[i] > mx:
        mx = a[i]
        char = chr(i)

print(char)

s = open('tests.txt').read().count('K')
print(s)