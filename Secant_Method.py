import math
a1 = float(input("First initial approximation : "))
a2 = float(input("Second initial approximation : "))

def ia(x):
    y = 3*x**3 + 10*x**2 + 10*x + 7
    return y
print(ia(a1),ia(a2))
z = (a1*ia(a2) - a2*ia(a1))/(ia(a2)-ia(a1))
print("\r")
for i in range(3):
        print(i+1,round(z,6))
        a1 = a2
        a2 = z
        try :
            z = (a1*ia(z) - a2*ia(a1))/(ia(a2)-ia(a1))
        except :
            print("Zero Division Error")

    
    
