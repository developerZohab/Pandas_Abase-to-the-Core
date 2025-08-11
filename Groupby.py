import pandas as pd

df = pd.read_csv("students_with_names.csv")
print(df)

print("Grup Section and Percentage")
g = df.groupby("Section")["Percentage"].max()
print(g)

print("After reset the index")
g = df.groupby(["Name", "Section"])["Percentage"].max().reset_index()
print(g)
