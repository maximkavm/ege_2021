print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = ((x or y) and not(z) and not(z == x))
            if F == True:
                print(x,y,z)