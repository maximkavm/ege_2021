s = '>' + 20 * '3' + 22 * '4' + 10 * '5'
while '>1' in s or '>2' in s or '>3' in s:
    if '>3' in s:
        s = s.replace('>3', '44>', 1)
    if '>4' in s:
        s = s.replace('>4', '4>', 1)
    if '>5' in s:
        s = s.replace('>5', '3>', 1)
print(s)
sm = 0
for i in range(len(s)):
    if s[i] != '>':
        sm += int(s[i])
print(sm)