import numpy as np

arr=np.array([1,2,3,4,5])
print(arr+4)
print(arr*4)
print('========ADD=========') 


matrix=np.arange(11,20).reshape(3,3)
matrix2=([1,2,3],[4,5,6],[7,8,9],)

'''NumPy broadcasting is a powerful mechanism that allows arithmetic operations on
 arrays of different shapes and/or dimensions. 
 Instead of making actual copies of the smaller array (which is memory-inefficient), 
 NumPy conceptually "stretches" it to match the larger array's shape for the operation

 NumPy Broadcasting Rules
 1. Dimension Padding
 2. Dimension Compatibility=Two dimensions are considered compatible if they meet one of two conditions:
-> They are the same size.
-> One of them has a size of 1.

 '''
#matrix add
A=np.array([1,2,3])
print(matrix+A)
print('---------------------') #DIIFERENT DIMENSION BUT SAME SIZE

print(matrix+matrix2)
print('========SUB=========')  #SAME DIMENSION

#matrix sub
print(matrix-matrix2)
print('=========MUL.=======')

#matrix mul
print(matrix*matrix2)
print('========DIV.=========')

#matrix div
print(matrix//matrix2)
print('================')

A=np.arange(1,10).reshape(3,3)
B=np.arange(10,19).reshape(3,3)
print(A+B)

