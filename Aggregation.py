import pandas as pd

df = pd.read_csv("students_with_names.csv")
print(df)

print("Calculation Average percentage")
g = df["Percentage"].mean()
print(g)

print("Calculation sum of total")
g = df["Total"].sum()
print(g)

print("Calculation max of percentage")
g = df["Percentage"].max()
print(g)


print("Calculation min of percentage")
g = df["Percentage"].min()
print(g)

print("Calculation median of percentage")
g = df["Percentage"].median()
print(g)

print("Calculation max of percentage")
g = df["Percentage"].std()
print(g)