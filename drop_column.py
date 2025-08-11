import pandas as pd

fg = pd.read_csv(r"C:\Users\Zohab\Desktop\Dhaval\week 3,4\Pandas\students_with_names.csv")
print(fg)
fg.drop(columns=['Arts','Social_Studies'], inplace=True)
print(fg) 