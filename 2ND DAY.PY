import numpy as np  #np is a alias:

list1=[1,2,3,4,5,6]
array=np.array(list1)**2
print(array)

a=(np.arange(1,100))
print(a)

print(a.ndim)

print(a.shape)
li4=[[1,2,3],[4,5,6],[7,8,9]]

list2=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
b=np.array(list2)
print(b)

print(np.ndim(list2))
print(np.shape(list2))

#this function is used for ones
x=np.ones((4,5),dtype=int)
print(x)

y=np.zeros((3,5),dtype=int)
print(y)

z=np.arange(1,101)
print(z)

print(z.reshape(10,10))


