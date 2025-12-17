#Find the shape, size, number of dimensions, and data type of a given array.

import numpy as np
a=np.arange(1,10).reshape(3,3)
print(a.shape)
print(a.size)
print(a.ndim)