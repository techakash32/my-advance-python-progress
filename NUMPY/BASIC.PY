import numpy as np

# -----------------------------------------------------
# 🌟 NUMPY: Numerical Python
# Numpy is used for fast mathematical operations on arrays.
# It supports multidimensional arrays, matrix operations,
# random number generation and vectorized computation.
# -----------------------------------------------------

# -----------------------------------------------------
# 1️⃣ Creating simple array + vectorized operation
# -----------------------------------------------------
list1 = [1, 2, 3, 4, 5]
array = np.array(list1) ** 10     # Each element power 10
print(array)

# -----------------------------------------------------
# 2️⃣ Heterogeneous list → Array of type OBJECT
# (Mixed data types become object array)
# -----------------------------------------------------
list2 = [1, 2.5, 'hello', True]
array2 = np.array(list2)
print(array2)
print("Array Data Type:", array2.dtype)

# -----------------------------------------------------
# 3️⃣ Homogeneous list → Converted to array (numeric/string)
# (All elements converted to common data type)
# -----------------------------------------------------
list3 = [1, 2.5, 'hello', True]
array3 = np.array(list3)
print(array3)
print("Array Data Type:", array3.dtype)

print("--------------------------------")

# -----------------------------------------------------
# 4️⃣ Creating 2D Array (Matrix)
# -----------------------------------------------------
list4 = [[1,2,3],[4,5,6],[7,8,9]]
array4 = np.array(list4)
print(array4)

print("--------------------------------")

# -----------------------------------------------------
# 5️⃣ Creating 3D Array (Tensor)
# -----------------------------------------------------
list5 = [
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]],
    [[13,14,15],[16,17,18]]
]
array5 = np.array(list5)
print(array5)
print("Array Dimension:", array5.ndim)

print("--------------------------------")

# -----------------------------------------------------
# 6️⃣ Checking shape & dimension
# -----------------------------------------------------
print("Array Shape array4:", array4.shape)
print("Array Dimension array5:", array5.ndim)

print("--------------------------------")

# -----------------------------------------------------
# 7️⃣ arange(start, stop, step)
# Creates array in a range (end EXCLUDED)
# -----------------------------------------------------
array6 = np.arange(1, 20, 2)
print(array6)

print("--------------------------------")

# -----------------------------------------------------
# 8️⃣ linspace(start, end, num_points)
# Creates evenly spaced numbers (end INCLUDED)
# -----------------------------------------------------
array7 = np.linspace(1, 10, 5)
print(array7)

print("--------------------------------")

# -----------------------------------------------------
# 9️⃣ zeros()
# Creates array filled with 0
# -----------------------------------------------------
array8 = np.zeros((3, 4))
print(array8)

print("--------------------------------")

# 🔟 ones()
# Creates array filled with 1 (default float)
# dtype=int → convert to integer
# -----------------------------------------------------
array9 = np.ones((2, 5), dtype=int)
print(array9)

print("--------------------------------")

# -----------------------------------------------------
# 1️⃣1️⃣ Identity matrix (Square)
# -----------------------------------------------------
array10 = np.eye(4, dtype=int)
print(array10)

print("--------------------------------")

# -----------------------------------------------------
# 1️⃣2️⃣ Random values (0 to 1)
# -----------------------------------------------------
array11 = np.random.rand(3, 3)
print(array11)

print("--------------------------------")

# -----------------------------------------------------
# 1️⃣3️⃣ Random integers
# -----------------------------------------------------
array12 = np.random.randint(1, 100, (4, 4))
print(array12)

print("--------------------------------")

# -----------------------------------------------------
# 1️⃣4️⃣ Reshaping array
# -----------------------------------------------------
array13 = np.arange(1, 13)
print("Original Array:", array13)

array14 = array13.reshape((3, 4))
print("Reshaped Array:\n", array14)

print("--------------------------------")

# -----------------------------------------------------
# 1️⃣5️⃣ Flatten array (convert to 1D)
# -----------------------------------------------------
array15 = array14.flatten()
print("Flattened Array:", array15)

print("--------------------------------")

# -----------------------------------------------------
# 1️⃣6️⃣ Slicing Array (2D)
# array[row_start:row_end , col_start:col_end]
# -----------------------------------------------------
array16 = array14[1:3, 1:4]
print("Sliced Array:\n", array16)

print("--------------------------------")

# Quick Example (reshape + arange)
print(np.arange(1, 13).reshape(3, 4))

# -----------------------------------------------------
# Summary of Important Numpy Functions:
'''
reshape     → change shape without changing data
zeros       → array of zeros
ones        → array of ones
eye         → identity matrix
arange      → range-based array
linspace    → evenly spaced values
flatten     → convert to 1D
random      → generate random values
slicing     → extracting subarrays
shape       → returns shape (rows, columns...)
ndim        → dimension of array
dtype       → data type
mixed dtype → numpy converts to common type
'''
# -----------------------------------------------------
