#Reshape a 1D array of 16 elements into a 4×4 matrix.
import numpy as np

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
array1=np.array(list)
array14 = array1.reshape((4, 4))
print(array14)