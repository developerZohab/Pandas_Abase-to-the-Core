import pandas as pd

print("Finding the missing Value")
f = {
    "Shift":["Ali", "Zopash", "Afaf", "Juniad", "Zohaib", None],
    "Age": [10, 11, 12, None, 14, 15],
    "Money": [56, 34, 79, 20, 5, None]
}

df = pd.DataFrame(f)

print("linear")
print(df)
df[["Age", "Money"]] = df[["Age", "Money"]].interpolate(method="linear")
print(df)


print("Slinear")
df[["Age", "Money"]] = df[["Age", "Money"]].interpolate(method="polynomial")
print(df)