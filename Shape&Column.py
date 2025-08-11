import pandas as pd

print("Shape of data:")

f = pd.read_csv("students_with_names.csv")

# Shape of the DataFrame
print("Shape : ",f.shape) #(no of ROWS, no of COLUMNS)

# Columns of the DataFrame
print("Column Names : ",f.columns) #Name of Columns
