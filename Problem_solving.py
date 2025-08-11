import pandas as pd

f = pd.read_csv("students_with_names.csv")

print(f)

print("SElecting single column")
g = f["Name"] # Selecting single column 
print(g)

print("Selecting multiple column")
h = f[["Name","Total","Percentage"]] # Selecting multiple column
print(h)


#2- Filter the Rows
# Boolean Indexing (True || False)
#   a. for Single Rows
#       r = df[df["Column Name] > 50]

print("Filtering Data by single column")
r = f[f["Percentage"] > 80] # Filter data by uising column
print(r)

print("Filtering Data by single column")
p = f[(f["Percentage"] > 80) & (f["Section"] == "A")]  # ✅ Correct way
print(p)

#   b. for Multiple Rows
#       r = df[(df["Column Name] > 50) & (df["Column Name 2] >= 30) ]
