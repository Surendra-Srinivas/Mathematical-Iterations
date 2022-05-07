#If the system is not diagonally dominant, exchange the equations,if possible,such that the new system is diagonally dominant 
# and convergence is guaranteed.

print("=======================")
a11 = float(input("Enter a11 : "))
a12 = float(input("Enter a12 : "))
a13 = float(input("Enter a13 : "))
print("=======================")
a21 = float(input("Enter a21 : "))
a22 = float(input("Enter a22 : "))
a23 = float(input("Enter a23 : "))
print("=======================")
a31 = float(input("Enter a31 : "))
a32 = float(input("Enter a32 : "))
a33 = float(input("Enter a33 : "))
print("=======================")
b1 = float(input("Enter b1 : "))
b2 = float(input("Enter b2 : "))
b3 = float(input("Enter b3 : "))


x2 = 0
x3 = 0
print("=======================")
for i in range(15):
    x_1 = (1/a11)*(b1 - a12*x2 - a13*x3)
    x_2 = (1/a22)*(b2 - a21*x_1 - a23*x3)
    x_3 = (1/a33)*(b3 - a31*x_1 - a32*x2)
    print(i+1,"   =   ",round(x_1,5),round(x_2,5),round(x_3,5))
    x2 = x_2
    x3 = x_3
print("=======================")
print(a11*x_1+a12*x_2+a13*x_3-b1)
print("=======================")
