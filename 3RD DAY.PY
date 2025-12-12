import numpy as np

#2d array using list:
li=[[1,2,3],[4,5,6],[7,8,9]]
array=np.array(li)

#using line sapace create 2d array:
x=np.linspace(10,20,6).reshape(3,2)
print(x)

#using arange create 2d list:
s=np.arange(1,13).reshape(3,4)
print(s)

#indexxing in numpy:
#access the element using the index as array is know as indxing.
#0-based index
s=np.array([1,2,3,4,5])
print(s[0])
print(s[-1])

print("----------------------------")
lst=[1,2,3,4,5]
for i in range(-5,0):
    print(lst[i])

print("===========================")

lst=[1,2,3,4,5]
for i in range(-1,-6,-1):
    print(lst[i])

print("----------------------------")

#slicing is used to find and exract array and sub array in numpy:
a=[1,2,3,4,5]
print(a[1:4])
#steps
print(a[1:6:2])

x=np.arange(1,5)
print(x[::-1])
print("++++++++++++++++++++++++++++")
#---matrix operation:

matrix=np.arange(1,13).reshape(3,4)
print(matrix[0])
print(matrix[0][0])  #[rows],[element index]
print("==========================")
for i in range(0,4):
    for j in range(i+1,4):
        print(matrix[i],[j])