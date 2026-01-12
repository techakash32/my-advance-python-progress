'''
====================================================================
📌 MATRIX OPERATIONS — ML NOTES (FULL COPY VERSION)
====================================================================

In Machine Learning, data is stored and processed using **matrices**.
A matrix is a 2-dimensional array of numbers arranged in rows & columns.

WHY ARE MATRICES USED IN ML?
----------------------------
✔ To store datasets (rows = samples, columns = features)  
✔ To perform fast mathematical operations  
✔ To represent images, signals, vectors  
✔ To compute transformations (rotation, scaling, projection)  
✔ To implement linear algebra in ML models  
✔ Used in: Linear Regression, Neural Networks, PCA, SVM, Deep Learning  

====================================================================
# 1️⃣ MATRIX ADDITION
# ---------------------------------------------------------------
DEFINITION:
Add two matrices element-wise.  
→ Both matrices must have SAME shape.

Example:
A + B

[1 2]   +   [4 5]   =   [5 7]
[3 4]       [6 7]       [9 11]

USE IN ML:
✔ Updating weights  
✔ Combining intermediate results  
✔ Feature engineering  
====================================================================

# 2️⃣ MATRIX SUBTRACTION
# ---------------------------------------------------------------
Same as addition but subtract element-wise.

[5 6]  –  [1 2]  =  [4 4]
[7 8]     [3 4]     [4 4]

USE IN ML:
✔ Calculating error (prediction – actual)  
✔ Gradient calculation  
====================================================================

# 3️⃣ SCALAR MULTIPLICATION
# ---------------------------------------------------------------
Multiply every matrix element by a constant value.

k × A

2 × [1 2]  =  [2 4]
    [3 4]     [6 8]

USE IN ML:
✔ Learning rate scaling  
✔ Feature scaling  
✔ Adjusting weight updates  
====================================================================

# 4️⃣ MATRIX MULTIPLICATION (DOT PRODUCT)
# ---------------------------------------------------------------
MOST IMPORTANT OPERATION IN ML & DEEP LEARNING.

RULE:
Columns of A must equal rows of B.

(A is m×n) × (B is n×p) → result is m×p

Example:
[1 2] × [5 6] = [1*5 + 2*7   1*6 + 2*8]
[3 4]   [7 8]   [3*5 + 4*7   3*6 + 4*8]

USE IN ML:
✔ Neural network forward propagation  
✔ Linear Regression predictions  
✔ Transforming data  
✔ Embeddings in NLP  
✔ Deep learning tensor operations  
====================================================================

# 5️⃣ MATRIX TRANSPOSE
# ---------------------------------------------------------------
Flip rows into columns.

Aᵀ = transpose(A)

[1 2]ᵀ = [1 3]
[3 4]    [2 4]

USE IN ML:
✔ Required for dot products  
✔ Covariance matrix computation (PCA)  
✔ Feature correlation analysis  
====================================================================

# 6️⃣ MATRIX INVERSE
# ---------------------------------------------------------------
Matrix A⁻¹ such that:

A × A⁻¹ = Identity matrix (I)

Only square matrices with non-zero determinant have an inverse.

USE IN ML:
✔ Solving Linear Regression equation:  
  θ = (XᵀX)⁻¹Xᵀy  
✔ Optimization  
✔ Transformations  
====================================================================

# 7️⃣ MATRIX DETERMINANT
# ---------------------------------------------------------------
A scalar value representing matrix properties.

USE IN ML:
✔ Checks if matrix is invertible  
✔ Used in PCA, covariance calculations  
✔ Stability in numerical computations  
====================================================================

# 8️⃣ IDENTITY MATRIX
# ---------------------------------------------------------------
Matrix with 1 on diagonal, 0 elsewhere.

[1 0]
[0 1]

USE IN ML:
✔ Base for matrix inverse  
✔ No change when multiplied: A × I = A  
✔ Regularization (Ridge Regression):  
  (XᵀX + λI)  
====================================================================

# 9️⃣ MATRIX RANK
# ---------------------------------------------------------------
Number of linearly independent rows/columns.

USE IN ML:
✔ Detect multicollinearity  
✔ Dimensionality reduction (PCA)  
✔ Understanding dataset variability  
====================================================================

# 1️⃣0️⃣ WHY MATRIX OPERATIONS ARE IMPORTANT IN ML
# ---------------------------------------------------------------
✔ ML models are based on **Linear Algebra**  
✔ Neural Networks = matrix multiplications on every layer  
✔ Training = repeated matrix operations on large datasets  
✔ GPU acceleration works because matrices are parallelizable  
✔ Faster computation time  
✔ Efficient storage  
✔ Clean mathematical representation  

====================================================================
SUMMARY
====================================================================

✔ Matrix = 2D data structure  
✔ Important operations:
    ➤ Addition  
    ➤ Subtraction  
    ➤ Scalar multiplication  
    ➤ Matrix multiplication  
    ➤ Transpose  
    ➤ Inverse  
    ➤ Determinant  
    ➤ Rank

✔ Used heavily in ML algorithms like:
    → Linear Regression  
    → Logistic Regression  
    → PCA  
    → SVM  
    → Neural Networks  
    → Deep Learning  

END OF NOTES.
====================================================================
'''
