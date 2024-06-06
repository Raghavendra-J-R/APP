"""
i.	Display only first two rows
ii.	Display only last two rows
iii.	 Extract the py-score of Toronto column.
iv.	Display of loc of last row

"""

import pandas as pd

# Create the DataFrame from the provided data
data = {
    "Name": ["Ann", "Xavier", "Jana", "Yi"],
    "City": ["Toronto", "Mexico City", "Prague", "Shanghai"],
    "Age": [41, 28, 33, 38],
    "Py-score": [89.0, 88.0, 81.0, 68.0],
}
df = pd.DataFrame(data)

# i) Display only the first two rows
print("First two rows:")
print(df.head())

# ii) Extract only the last two rows
print("\nLast two rows:")
print(df.tail(2))

# iii) Display the Py-score of Toronto
toronto_py_score = df[df["City"] == "Toronto"]["Py-score"].values[0]
print(f"\nPy-score of Toronto: {toronto_py_score:.2f}")

# iv) Calculate mean, min, max, and standard deviation for the Age column
age_mean = df["Age"].mean()
age_min = df["Age"].min()
age_max = df["Age"].max()
age_std = df["Age"].std()
print(f"\nAge statistics:")
print(f"Mean: {age_mean:.2f}")
print(f"Min: {age_min}")
print(f"Max: {age_max}")
print(f"Standard Deviation: {age_std:.2f}")

# v) Calculate the loc of the last row
last_row = df.iloc[-1]
print("\nLast row:")
print(last_row)

# vi) Print basic stats using the describe() method
print("\nBasic stats using describe():")
print(df.describe())
