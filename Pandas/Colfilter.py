"""

-------------------------------------------------------------------------
1. Select specific Column
2. filter Rows
3. Combine multiple conditions

--------------------------------------------------------------------------

1. Square bracket (If we want to access the column then we can use sqaure bracket)
2. Boolean condition (If you want to filter the rows then you can use the boolean condition)

--------------------------------------------------------------------------

Selecting specific columns from specific data
1. A series (selecting single column)
2. dataframe multiple column of data 

column = df["Column Name"] ---------- single column selection
column = df["column1","column2", "column3"]

--------------------------------------------------------------------------

Filtering Rows
1. we use Boolean indexing 

------------Based on single condition
filtered_rows = df[df["Salary"] > 50000]


------------Combine multiple condition
filtered_rows = df[(df["col1"] > value) & (df["col2"] < value)]

--------------------------------------------------------------------------
"""


import pandas as pd


data = {
    "Name": ['Ram', 'Shyam','Ghanshyam', 'Dhanshyam', 'Aditi','Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32] ,
    "Salary":[50000,60000,45000,52000,49000, 70000, 48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80, 89]
}

df = pd.DataFrame(data)

print("Sample Dataframe")
# print(df)

print("Name (Single Column access--- series)")
print(df["Name"])


# selecting multiple columns
subset = df[["Name","Salary"]]
print(subset)