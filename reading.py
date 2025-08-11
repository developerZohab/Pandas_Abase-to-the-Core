import pandas as pd

fg = pd.read_csv(r"C:\Users\Zohab\Desktop\Dhaval\week 3,4\Pandas\students_with_names.csv")
#fg = pd.read_csv(r"C:\Users\Zohab\Desktop\Dhaval\week 3,4\Pandas\students_with_names.csv", encoding="latin1","gcfx(for big data stored on google cloud","UTF-8")")# iff your facing issue in reading file
#fg = pd.read_csv("C:\\Users\\Zohab\\Desktop\\Dhaval\\week 3,4\\Pandas\\students_with_names.csv")
#fg.to_excel("students_with_names.xlsx", index=False) # convert data from csv to excel
fg.to_json("students_with_names.json", index=True) # no index



g = pd.read_json(r"C:\Users\Zohab\Desktop\Dhaval\week 3,4\Pandas\students_with_names.json")
print(g)


