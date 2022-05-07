import numpy as x
arr = x.array([[1,10,-3,3],[2,3,20,7],[10,-1,2,4]])
print(arr)

a11 = arr[0][0]
a12 = arr[0][1]
a13 = arr[0][2]
a14 = arr[0][3]

a21 = arr[1][0]
a22 = arr[1][1]
a23 = arr[1][2]

a31 = arr[2][0]
a32 = arr[2][1]
a33 = arr[2][2]
a34 = arr[2][3]

print("\r")
a =arr[1][0]-((a21/a11)*arr[0][0])
b = arr[1][1] -(a21/a11)*arr[0][1]
c = arr[1][2]-((a21/a11)*arr[0][2])
d = arr[1][3] - (a21/a11)*arr[0][3]
arr = x.array([[a11,a12,a13,a14],[a,b,c,d],[a31,a32,a33,a34]])
print(arr)



e = arr[2][0] -(a31/a11)*arr[0][0]
f= arr[2][1] -(a31/a11)*arr[0][1]
g= arr[2][2] -(a31/a11)*arr[0][2]
h= arr[2][3] - (a31/a11)*arr[0][3]
print("\r")
arr = x.array([[a11,a12,a13,a14],[a,b,c,d],[e,f,g,h]])
print(arr)


a31 = arr[2][1]
a21 = arr[1][1]
if arr[2][1] !=0:
    arr[2][0] = arr[2][0] -(a31/a21)*arr[1][0]
    arr[2][1] = arr[2][1] -(a31/a21)*arr[1][1]
    arr[2][2] = arr[2][2] -(a31/a21)*arr[1][2]
    arr[2][3] =  arr[2][3] -(a31/a21)*arr[1][3]
    print("\r")
    print(arr)
else : pass

if arr[2][1] ==0 and arr[2][2] != 0: 
    z = arr[2][3] / arr[2][2]
    y = (arr[1][3] - arr[1][2] * z) /  arr[1][1]
    x1 = (a14 - a12*y - a13*z) / a11
    print("\r")
    print('X = ',round(x1,4))
    print('Y = ',round(y,4))
    print('Z = ',round(z,4))
 
if arr[2][2] == 0:
    print("No solution")