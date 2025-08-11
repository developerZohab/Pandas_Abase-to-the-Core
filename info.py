import pandas as pd


print("getting information about data")
#1- Total number of Rows and Column
#2- Column Name
#3- Datatype
#4- Non-Null counts
#5- Mamory usage of dataframe(imp for big Data)

f = pd.read_csv("students_with_names.csv")
print(f.info())