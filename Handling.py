import pandas as pd


print("Finding the missing Value")
f = {
    "Name":["Zohab","Zopash","Afaf","Juniad","Zohaib",None],
    "Age" :[19,17,12,22,15,None],
    "Money" :[56,34,79,20,5,None]

}

df = pd.DataFrame(f)

df.dropna(axis =0, inplace = True)

print(df)