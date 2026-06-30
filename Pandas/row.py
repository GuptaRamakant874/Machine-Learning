# two method to check the row of data
# head() & tail()

# head(n)  -- n rows return from starting and if n not provided then by default return 5 rows
# tail(n)  -- n rows return from last and if n not provided then by default return 5 rows

import pandas as pd

df = pd.read_json("sample_Data.json")


print("Display 10 rows from first")
# print(df.head(10))
print(df.head()) # by default 5 rows show


# print("Display 10 rows from last")
# print(df.tail(10))