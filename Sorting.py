import pandas as pd

df = pd.read_csv("students_with_names.csv")

print(df)

print("Sorted data")
df.sort_values(by=["Total","Percentage"], ascending=False, inplace=True) # Sorted the data in Ascending order
print(df.head(20))
