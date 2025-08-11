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
a = pd.DataFrame(D)  # Create DataFrame from dictionary D
print(a) 
print()


print("Second dataset")
b = pd.DataFrame(F)
print(b)


print()
print("Inner join")
s = pd.merge(a, b, on="Roll no", how="inner")
print(s)

print()
print("Outer Join")
s = pd.merge(a, b, on="Roll no", how="outer")
print(s)

print()
print("Right Join")
s = pd.merge(a, b, on="Roll no", how="right")
print(s)

print()
print("Left Join")
s = pd.merge(a, b, on="Roll no", how="left")
print(s)


print()
print("Cross Join Result:")
cross_join_df = pd.merge(a, b, how="cross")
print(cross_join_df)