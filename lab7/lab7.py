"""
7. Implement a program to create a Data Frame which contains data given below:
"""

import pandas as pd

df = pd.DataFrame(
    [
        [30.20, 29.41, 29.87],
        [30.28, 29.32, 30.24],
        [30.45, 29.96, 30.10],
        [29.35, 28.74, 28.90],
        [29.35, 28.56, 28.92],
    ],
    columns=["High", "Low", "Close"],
    index=["2009-02-11", "2009-02-12", "2009-02-13", "2009-02-17", "2009-02-18"],
)

s = pd.Series([True, False, False, True, False], name="bools")

print(df[s.values])
