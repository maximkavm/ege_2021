print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = (not(z) and x)
            if F == True:
                print(x,y,z)