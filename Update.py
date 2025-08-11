import pandas as pd

fg = pd.read_csv(r"C:\Users\Zohab\Desktop\Dhaval\week 3,4\Pandas\students_with_names.csv")

fg.loc[0,'Total'] = 420 # fg.loc[index,'Column name'] = updated value
print(fg)

fg['Total'] = fg['Total'] +20

print(fg)