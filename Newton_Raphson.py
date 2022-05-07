def func(x):
    y = x**4 - 3*x**2 + x - 10
    return y
def func_(n):
    y_ = 4*x**3 - 6*x + 1
    return y_
x = 2.15625
for i in range(6):
    t = x - (func(x)/func_(x))
    print(round(t,10),end = " ")
    x = t
    #print(round(func(x),5),round(func_(x),5))

