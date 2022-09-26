def f(x):
    return x**3 - 3*x**2 - x + 3

def simple_operation(x, a, b):
    return x - f(x) * (b - a) / (f(b) - f(a))

e = 0.001

x = -1.5

while f(x + e) * f(x - e) >= 0:
    x = simple_operation(x, -1.5, -0.5)
    print(x)