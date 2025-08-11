import pandas as pd


print("Grtting Detail Describtion about data")


f = pd.read_csv("students_with_names.csv")
print(f.describe())