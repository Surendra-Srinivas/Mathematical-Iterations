import math

a1 = float(input("First initial approximation : "))
a2 = float(input("Second initial approximation : "))

def func(x):
    y = 3*x**3 + 10*x**2 + 10*x + 7
    return y
if func(a1)*func(a2) < 0:
    for i in range(2):
        c = (round(a1,7)+round(a2,7))/2
        temp = func(c)
        print("===========")
        print("Iteration : ",i)
        print("A Positive root lies between : ",round(a1,7),"and",round(a2,7))
        print(round(c,7),"= x")
        print(round(temp,7),"=  f(x)")
        print(round(func(a1)*func(c),10))
        if func(c) > 0:
            a2 = c
        if func(c)<0:
            a1 = c
print("===========")


        

