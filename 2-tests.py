print("x y z w")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x and y) or (y and z)) == ((not(x) or w) and (not(w) or z))
                if F == True:
                    print(x, y, z, w)