import pandas as pd

data = {
    "Name":["Ram","Mohan","RK"],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Anand']
}

df = pd.DataFrame(data)

print(df)

df.to_csv("output.csv",index=False) # this converting to csv file and save in your folder without index

# you can do this as for the excel and json also
# df.to_excel("output.xlsx")
df.to_json("out.json",index=False)