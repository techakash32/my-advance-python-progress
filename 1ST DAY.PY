import numpy as np
list=[1,2,3,4,5]
array=np.array(list)**10
print(array)

#heterogeneous list: it will convert to array of type object

list2=[1,2.5,'hello',True]
array2=np.array(list2)
print(array2)
#hydrogenous list: it will convert to array of type string

list3=[1,2.5,'hello',True]
array3=np.array(list3)
print(array3)

print("--------------------------------")
#creating 2D array
list4=[[1,2,3],[4,5,6],[7,8,9]]
array4=np.array(list4)
print(array4)

print("--------------------------------")

#creating 3D array
list5=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]]
array5=np.array(list5)
print(array5)
print("Array Dimension:",array5.ndim)

print("--------------------------------")

#checking array shape:
print("Array Shape:",array4.shape)
print("Array Shape:",array5.ndim)
print("--------------------------------")

#creating array using arange
array6=np.arange(1,20,2)
print(array6)

print("--------------------------------")

#creating array using linspace
array7=np.linspace(1,10,5)
print(array7)

print("--------------------------------")

#creating array using zeros
array8=np.zeros((3,4))
print(array8)
print("--------------------------------")

#creating array using ones
array9=np.ones((2,5),dtype=int)  #IT PASS FLOAT BY DEFAULT
# WE CAN CHANGE IT BY dtype=int
print(array9)
print("--------------------------------")

#creating identity matrix
array10=np.eye((4),dtype=int)
print(array10)   
print("--------------------------------")

#creating random array
array11=np.random.rand(3,3)
print(array11)
print("--------------------------------")

#creating random integer array
array12=np.random.randint(1,100,(4,4))
print(array12)

print("--------------------------------")

#reshaping array
array13=np.arange(1,13)
print("Original Array:",array13)
array14=array13.reshape((3,4))
print("Reshaped Array:\n",array14)

print("--------------------------------")

#flattening array
array15=array14.flatten()
print("Flattened Array:",array15)
print("--------------------------------")

#slicing array
array16=array14[1:3,1:4]
print("Sliced Array:\n",array16)
print("--------------------------------")

#arange funcition create an array in a range(start,end,step)-> exculsive of end

print(np.arange(1,13).reshape(3,4))

#numpy basic operations:
'''
reshape
zeros
ones
eye
arange
linspace
flatten
random
slicing
shape
ndim
linespace
dtype
mixdtype

'''
