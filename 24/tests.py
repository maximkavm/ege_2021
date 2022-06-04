file = open("tests.txt")

string = file.read()
string = string.replace("CB", "AB")

for i in range(1000):
    if i*"AB" in string:
        print(i)