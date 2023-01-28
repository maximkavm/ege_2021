import itertools

words = set()

s = 'капкан'

for p in itertools.permutations(s):
    w = ''.join(p)
    if w.count('аа') == 0 and w.count('кк') == 0:
        words.add(w)

print(len(words))