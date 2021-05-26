import itertools

i = 0
for x in itertools.product('МЫШКА', repeat=6):
    if ''.join(x).count('ЫШ') >= 2:
        i += 1
print(i)