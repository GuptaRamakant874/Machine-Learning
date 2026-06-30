import pandas as pd

# read data from the CSV file and Excel file into a dataframe
# df = pd.read_csv("titanic.csv")
# df = pd.read_excel("Student.xlsx" , engine="openpyxl")
df = pd.read_json("sample_Data.json")

print(df)