import pandas as pd

data = {
    "Name":["Ram","Mohan","RK"],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Anand']
}

df = pd.DataFrame(data)

print("displaying the info of dataset")
print(df.info())