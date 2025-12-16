import pandas as pd
import numpy as np

print("=====================================================")

df = pd.read_csv('sample_students_data.csv')
student_detail = {
    'name': ['Rahul', 'Naman', 'Aman'],
    'subject': ['Maths', 'English', 'Social Science'],
    'marks': [50, 60, 70],
    'address': ['Jaipur', 'MP', 'Delhi']
}

df_students = pd.DataFrame(student_detail)
print(df_students)

#converting a data frame to csv format:

df_students.to_csv("akash.csv")
print("=====================================================")

# --converting data frame to excel
df_students.to_excel("akashnagar2.xlsx")

#select only one coloumn in dataset:

print(df_students.columns)
print("=====================================================")

#selecting multiple coloumn:
print(df_students[['name','subject']])
print("=====================================================")

#select only one row

print(df_students.loc[0])
print(df_students.loc[0:5])  #into this slicing end is include:
#df.loc is used to retrive the particular rowusing the label:
print("=====================================================")

print(df_students.loc[0:2, ['name','subject','marks']])
# --print(df_students.loc[['0','1','2'['name','subject']]])
print("=====================================================")

# question: print 3 coloumn and all row: 
print(df_students.loc[:,['name','subject','marks']])

'''
loc=The .loc[] attribute in pandas is the primary method used 
for label-based indexing to select or modify a group of rows 
and columns in a DataFrame. It uses the actual row and columnnames
(labels) rather than their integer positions. 
Key Characteristics

1. Label-Based:
 It strictly uses the row and column labels provided in the DataFrame's index.

2. Inclusive Slicing: 
When slicing (e.g., 'a':'f'), both the start 
and the stop labels are included in the result, which is 
different from standard Python slicing that typically excludes 
the stop index.

iloc:= The .iloc in pandas is a way to pick data from a table
 (DataFrame) by its position or location, using simple numbers.
It's like finding a seat in a theater:
You don't say, "Find the seat labeled 'A10'."
Instead, you say, "Go to the first row and the tenth seat."
With .iloc:
The first row is number 0.
The second column is number 1.
df.iloc[0, 1] gets the value at the very first row and the second column.

'''
print("===================================================")
print(df_students.iloc[0:2,0:2])


