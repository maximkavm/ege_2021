import itertools

i = 0
for x in itertools.product('СОЛЬ', repeat=4):
    if ''.join(x).count('ОЬ') == 0 and ''.join(x)[0] != 'Ь':
        print(i, ''.join(x))
        i += 1
print(i)