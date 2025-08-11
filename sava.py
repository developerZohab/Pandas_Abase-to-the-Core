import pandas as pd

data ={
   "Name":["Ali","Veer","Goga"],
   "Age":[12,45,67],
   "Budget":[10000,45000,78450]
}

g = pd.DataFrame(data, index =False)
print(g)