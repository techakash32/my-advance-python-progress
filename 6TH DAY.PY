import pandas as pd
import numpy as np

# --------------------------------------------------
# Pandas:
# Pandas is a powerful Python library used for
# data manipulation and data analysis.
# It provides two main data structures:
# 1) Series (1D)
# 2) DataFrame (2D)
# --------------------------------------------------

# Reading a CSV file (example)
# Note: This returns a DataFrame, so we store it in a variable
df = pd.read_csv('sample_students_data.csv')

# --------------------------------------------------
# Creating a Series using NumPy array
# --------------------------------------------------
x = pd.Series(np.array([1, 2, 3, 4]), index=['a', 'b', 'c', 'd'])

print(x)
print("Shape :", x.shape)   # Number of elements as a tuple
print("Size  :", x.size)    # Total number of elements
print("Dim   :", x.ndim)    # Number of dimensions

print('============================')

# --------------------------------------------------
# Creating a Series using a List
# --------------------------------------------------
li = [1, 2, 3, 4]
li_idx = ['a', 'b', 'c', 'd']

series_from_list = pd.Series(li, index=li_idx)
print(series_from_list)

print("===== using dictionary =====")

# --------------------------------------------------
# Creating a Series using a Dictionary
# --------------------------------------------------
d = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}

series_from_dict = pd.Series(d)
print(series_from_dict)

print("===== vectorized operations =====")

# --------------------------------------------------
# Vectorized Operations in Series
# (Operations are applied element-wise)
# --------------------------------------------------
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

print("Addition:\n", s1 + s2)
print("Subtraction:\n", s1 - s2)

# Accessing element using index position
print("Element at index 1:", s1[1])

print("=========== ACCESS ELEMENTS =========")

# --------------------------------------------------
# Conditional Selection in Series
# --------------------------------------------------
SERIES = pd.Series(np.arange(1, 13))

# Elements greater than 5
print(SERIES[SERIES > 5])

# Even numbers
print(SERIES[SERIES % 2 == 0])

print("======== DATAFRAME ========")

"""
DataFrame:
A DataFrame is a two-dimensional, tabular data structure
used for data manipulation and analysis in Python.

It is similar to:
- An Excel spreadsheet
- A table in a SQL database

Data is organized into rows and columns.
"""

# --------------------------------------------------
# Creating DataFrame using a Dictionary
# --------------------------------------------------
student_detail = {
    'name': ['Rahul', 'Naman', 'Aman'],
    'subject': ['Maths', 'English', 'Social Science'],
    'marks': [50, 60, 70],
    'address': ['Jaipur', 'MP', 'Delhi']
}

df_students = pd.DataFrame(student_detail)
print(df_students)

# --------------------------------------------------
# Creating DataFrame using a List (Row-wise)
# --------------------------------------------------
detail = [
    ['Rahul', 'Maths', 50, 'Jaipur'],
    ['Naman', 'English', 60, 'MP'],
    ['Aman', 'Social Science', 70, 'Delhi']
]

df_from_list = pd.DataFrame(
    detail,
    columns=['name', 'subject', 'marks', 'address']
)

print(df_from_list)
