a = [[], [], [], [], [], [], [], [], [], []]

for i in range(0, 2021):
    a[(i*i*i) % 10].append(i)

print(len(a[0]), len(a[1]),len(a[2]),len(a[3]),len(a[4]),len(a[5]),len(a[6]),len(a[7]),len(a[8]),len(a[9]))