import pandas as pd

print("Finding the missing Value")
f = {
    "Name": ["Zohab", "Zopash", "Afaf", "Juniad", "Zohaib", None],
    "Age": [19, 17, 12, 22, 15, None],
    "Money": [56, 34, 79, 20, 5, None]
}

df = pd.DataFrame(f)

# Fill missing Age and Name with the column mean
print("Handling multiple value")
df["Name"].fillna("Ali", inplace=True)
df[["Age", "Money"]] = df[["Age", "Money"]].fillna(df[["Age", "Money"]].mean())
print(df[["Age", "Money"]] )


# Fill all remaining missing values (Name and Money) with 0
df.fillna(0, inplace=True)
print(df)
