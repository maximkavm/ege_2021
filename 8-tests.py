import itertools

counter = 0

for i in itertools.permutations('вуаль'):
    word = ''.join(i)
    if (word.count('в') == 1 and word.count('у') == 1
        and word.count('а') == 1 and word.count('л') == 1
        and word.count('ь') == 1 and word[0] != 'ь' and
        word.count('ьу') == 0 and word.count('ьа') == 0):

        counter += 1

print(counter)
