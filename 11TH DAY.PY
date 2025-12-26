import pandas as pd
data = {
    'student_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [18, 19, 18, 20, 19],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'math': [90, 85, 92, 78, 88],
    'science': [95, 80, 89, 81, 94],
    'social_science': [88, 91, 85, 76, 90]
}

df = pd.DataFrame(data)

#finding total :
df['total']=df['math']+df['science']+df['social_science']/3

# make function for do pass and fail:
def assign(marks):
    if marks>=140:
        return 'pass'
    else:
        return 'fail'
df['pass/fail']=df['total'].map(assign)
print(df)

#rename

df.rename(columns={'name': 'student'}, inplace=True)
print(df)

df.drop(0, axis=0,inplace=True)
print(df)

df.reset_index()

print(df.iloc[:,2])

print(df.isnull().sum())

df['akash']:[1,2,3,4,5]
print(df)
