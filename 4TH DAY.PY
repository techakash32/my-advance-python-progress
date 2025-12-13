import numpy as np
#making the 2d array
matrix=np.arange(1,13).reshape(3,4)
print(matrix)

print("=================")

#access row: 
print(matrix[0][:])
print(matrix[0,:])
print(matrix[0:2,:]) #access two row

print("=================")

#access coloumn:
print(matrix[:,0])

print("=================")

#finding first two coloumn :
print(matrix[:, 0:2])

print(matrix[1:,2:]) #extract sub matrix

#watch youtube video
print("RANDOM NUMBER USING RANDINT")
#genrate array in given in given range: 
#the start is inclusive and end is exculsive: 
x=np.random.seed(34)
y=np.random.randint(99999,999999999,5)
print(x)

c=np.random.rand(10)
print(c)
#np.random is used to genrate the values between 0 to 1:

print("===================")

#mean find in array 
x=np.array([1,2,3,4])
print(np.mean(x))

#median find in array
u=np.random.randint(1,10,5)
print(u)  #with random number
print(np.median(u))

# Flatten array (convert to 1D)
# -----------------------------------------------------
r = matrix.flatten()
print("Flattened Array:", r)

n=matrix.ravel()
print("ravel array",n)

#flaten matrix
#Always a copy of the original array.
#Allocates new memory for the flattened array, making it slower and using more memory.	
#Modifying the flattened array does not affect the original array.	

#numpy.ravel()
#A view of the original array whenever possible; otherwise, a copy.
#Is more memory-efficient and generally faster as it avoids memory duplication when possible.
#Modifying the raveled array may change the original array's contents if a view was returned.
#Is a library-level function (np.ravel()) that can operate on any array-like object (e.g., Python lists, ndarrays).

