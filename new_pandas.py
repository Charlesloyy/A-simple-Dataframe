import pandas as pd
x = {
    "no": [1, 2, 3, 4, 5, 5, 6],
    "sum": [2, 2, 4, 5, 5, 5, 5]
    }
df = pd.DataFrame(x)
df.to_csv("new_pandas.csv")
print (df)
