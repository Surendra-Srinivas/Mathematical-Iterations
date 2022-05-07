import math
y = 0.6
for i in range(20):
    func = (1+math.cos(y))/3
    print(round(func,6))
    y = func

