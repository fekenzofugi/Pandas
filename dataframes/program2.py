import numpy as np
import pandas as pd

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5,4), np.array(['A', 'B', 'C', 'D', 'E']), np.array(['W', 'X', 'Y', 'Z']))
print(df)
print("-" * 100)

print("A boolean dataframe with the results greater than 0")
print(df > 0)
print("-" * 100)

print("NaN in the fields that are less than 0")
print(df[df > 0])
print("-" * 100)

print(df['W'] > 0)
print(df['W'])
print(df[df['W'] > 0])
print(df[df['W'] > 0]['X'])
print("-" * 100)

# multiple conditions
print(df[(df['W'] > 0) & (df['Y'] < 0)])
print("-" * 100)

# indexing
df.reset_index() # inplace = True to actually change the DataFrame
print(df)

newindex = 'CA NY WY OR CO'.split()
df["States"] = newindex
print(df)



