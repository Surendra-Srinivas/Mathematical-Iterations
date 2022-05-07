import math
def func(x):
    y = 3*x**3 + 10*x**2 + 10*x + 7
    return y
a = float(input("Enter first Approximation : "))
b = float(input("Enter Second Approximation : "))
for i in range(3):
    #const = func(b)
    t = (a*func(b)-b*func(a))/(func(b)-func(a))
    print(round(t,6))
    a = t