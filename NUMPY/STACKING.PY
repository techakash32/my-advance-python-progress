'''
====================================================================
📌 NUMPY STACKING (NOTES + EXAMPLES)
====================================================================

NumPy stacking is used to **join multiple arrays** along a specified axis.
It is widely used in **Data Science, ML, and Image Processing**.

WHY STACKING IS IMPORTANT?
--------------------------
✔ Combine multiple datasets  
✔ Prepare features for ML models  
✔ Merge images or matrices  
✔ Organize data efficiently  
✔ Perform batch operations  

====================================================================
# 1️⃣ np.stack()
# ---------------------------------------------------------------
DEFINITION:
Joins arrays along a **new axis**.

SYNTAX:
np.stack((arr1, arr2), axis=0)

RULE:
✔ All arrays must have SAME shape

Example:
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.stack((a, b))
Output:
[[1 2 3]
 [4 5 6]]

np.stack((a, b), axis=1)
Output:
[[1 4]
 [2 5]
 [3 6]]

USE:
✔ Create multi-dimensional arrays  
✔ Add new dimension  

====================================================================
# 2️⃣ np.vstack()  (Vertical Stacking)
# ---------------------------------------------------------------
DEFINITION:
Stacks arrays **row-wise** (top to bottom).

SYNTAX:
np.vstack((arr1, arr2))

Example:
np.vstack((a, b))

Output:
[[1 2 3]
 [4 5 6]]

USE:
✔ Add new rows  
✔ Combine datasets vertically  

====================================================================
# 3️⃣ np.hstack()  (Horizontal Stacking)
# ---------------------------------------------------------------
DEFINITION:
Stacks arrays **column-wise** (side by side).

SYNTAX:
np.hstack((arr1, arr2))

Example:
np.hstack((a, b))

Output:
[1 2 3 4 5 6]

USE:
✔ Add new features  
✔ Feature engineering  

====================================================================
# 4️⃣ np.dstack()  (Depth Stacking)
# ---------------------------------------------------------------
DEFINITION:
Stacks arrays along the **third axis (depth)**.

SYNTAX:
np.dstack((arr1, arr2))

Example:
np.dstack((a, b))

Output:
[[[1 4]
  [2 5]
  [3 6]]]

USE:
✔ Image processing (RGB channels)  
✔ 3D data representation  

====================================================================
# 5️⃣ DIFFERENCE BETWEEN STACKING METHODS
====================================================================

Method        | Axis Used | Result Dimension | Use Case
--------------|-----------|------------------|-----------------------------
stack()       | New axis  | Increases dim    | Add new dimension
vstack()      | axis=0    | Row-wise         | Add rows
hstack()      | axis=1    | Column-wise      | Add columns
dstack()      | axis=2    | Depth-wise       | 3D data / images

====================================================================
# 6️⃣ STACKING vs CONCATENATION
====================================================================

STACKING:
✔ Adds a new axis  
✔ Shape increases  

CONCATENATION:
✔ Merges along existing axis  
✔ No new dimension  

====================================================================
SUMMARY
====================================================================

✔ np.stack()  → adds new axis  
✔ np.vstack() → vertical merge  
✔ np.hstack() → horizontal merge  
✔ np.dstack() → depth merge  

✔ Used heavily in:
   → Machine Learning  
   → Data preprocessing  
   → Feature engineering  
   → Image processing  

END OF NOTES.
====================================================================
'''
'''
====================================================================
📌 NUMPY COPY vs VIEW (NOTES + EXAMPLES)
====================================================================

In NumPy, copying data can be done in **two ways**:
1️⃣ COPY  
2️⃣ VIEW  

Understanding this is **very important for ML & Data Science** because
it affects **memory usage and performance**.

====================================================================
# 1️⃣ NUMPY COPY
# ---------------------------------------------------------------
DEFINITION:
A COPY creates a **new array with its own data**.
Changes in the new array **do NOT affect** the original array.

METHOD:
.copy()

Example:
import numpy as np

a = np.array([10, 20, 30, 40])

b = a.copy()
b[0] = 99

print(a)   # [10 20 30 40]
print(b)   # [99 20 30 40]

KEY POINTS:
✔ Separate memory  
✔ Safe for data manipulation  
✔ Original data remains unchanged  

WHEN TO USE COPY?
✔ When original data must be protected  
✔ Data preprocessing in ML  
✔ Independent array operations  

====================================================================
# 2️⃣ NUMPY VIEW
# ---------------------------------------------------------------
DEFINITION:
A VIEW creates a **new array object** but **shares the same data**.
Changes in one array **affect the other**.

METHOD:
.view()

Example:
a = np.array([10, 20, 30, 40])

b = a.view()
b[0] = 99

print(a)   # [99 20 30 40]
print(b)   # [99 20 30 40]

KEY POINTS:
✔ Shares memory  
✔ Faster  
✔ Memory efficient  

WHEN TO USE VIEW?
✔ Large datasets  
✔ Performance-critical tasks  
✔ Memory optimization  

====================================================================
# 3️⃣ CHECK MEMORY SHARING
# ---------------------------------------------------------------
Use base attribute:

print(b.base)

✔ If base is NOT None → VIEW  
✔ If base is None → COPY  

Example:
a = np.array([1, 2, 3])
b = a.view()
c = a.copy()

print(b.base is a)   # True
print(c.base)        # None

====================================================================
# 4️⃣ COPY vs VIEW (DIFFERENCE TABLE)
====================================================================

Feature          | COPY                    | VIEW
-----------------|-------------------------|-------------------------
Memory           | New memory created      | Shared memory
Data Safety      | Safe                    | Not safe
Speed            | Slower                  | Faster
Memory Usage     | More                    | Less
Changes Affect   | Only new array          | Both arrays
Use Case         | Data protection         | Performance optimization

====================================================================
# 5️⃣ WHY COPY & VIEW ARE IMPORTANT IN ML?
====================================================================

✔ Prevent accidental data corruption  
✔ Optimize memory for large datasets  
✔ Faster matrix operations  
✔ Efficient data pipelines  

====================================================================
SUMMARY
====================================================================

✔ .copy() → Independent data  
✔ .view() → Shared data  
✔ COPY = Safety  
✔ VIEW = Performance  

END OF NOTES.
====================================================================

'''