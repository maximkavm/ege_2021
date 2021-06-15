print('w x y z')
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                F = ((y <= z) or (not(x) and w)) == (w == z)
                if F == True:
                    print(w,x,y,z)