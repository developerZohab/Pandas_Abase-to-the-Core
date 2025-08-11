import pandas as pd

D = {
    "Roll no": [1, 2, 3, 4,5,6,7,8],
    "Name": ["Ali", "Asad", "Kinat", "Mussa","Zoha","Zavi","Mali","Fasi"],
    "Age": [12, 14, 15, 18, 15, 18, 14, 10],
    "subject" :["English","urdu","Math","Science","Arts","Computer","islamiyat","Drawing"]
}

F = {
    "Course": ["str", "dts", "gta", "ght"],
    "Roll no": [1, 2, 3, 4],
    "Teacher": ["Mr.Ali", "Mr.Waseem", "Mr.Liaqat", "Ms.Zara"]
}

print("First dataset")
print()
a = pd.DataFrame(D)  # Create DataFrame from dictionary D
print(a) 
print()

print()
print("Second dataset")
print()
b = pd.DataFrame(F)
print(b)

print()
print("Vertical concatination")
print()
g = pd.concat([a,b] , axis =0 ,ignore_index= True)
print(g)

print()
print("Horizontal concatination")
print()
g = pd.concat([a,b] , axis =1 ,ignore_index= True)
print(g)