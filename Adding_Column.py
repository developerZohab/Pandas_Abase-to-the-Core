import numpy as np
import pandas as pd

f = pd.read_csv("students_with_names.csv")

f["Comments"] = np.where(
    f["Percentage"] > 80, "Excellent Work! Keep it up",
    np.where(f["Percentage"] < 50, "Good",
    np.where(f["Percentage"] > 60, "Well Done",
    "Need Work Hard"))
)
print(f)

well_done_students = f[f["Comments"] == "Well Done"][["Name", "Percentage"]]
print(well_done_students)

# Insert a new column at position 9
f.insert(9, "Bata", range(1, len(f) + 1))

# Print the updated DataFrame
print(f)