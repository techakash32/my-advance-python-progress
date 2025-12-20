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
print("=====================================================")

#loc vs iloc: 
#loc
print(df_students.loc[[0, 1], ['name', 'subject']])
print("======================================================")

#iloc
print(df_students.iloc[[2], 0:2])

# df.iloc[row_slicing, column_slicing]
# df.loc[row_labels, column_labels]

import seaborn as sns

# 1. Load the dataset and assign it to a variable
df = sns.load_dataset("tips")

# 2. Print the unique values in the 'time' column
print(df['time'].unique())