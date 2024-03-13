import numpy as np
import pandas as pd

np.random.seed(101)

data = np.arange(1, 10).reshape(3, 3)
print("The data inside the dataframe is \n{}".format(data))

df = pd.DataFrame(data, np.array(['a', 'b', 'c']))
print("The DataFrame is equal to\n{}".format(df))
print(type(df))

column = df[0]
print("The column 0 =\n{}".format(column))
print("The data type of a single columns is a {}".format(type(column)))

columns_a_b = df[[0,1]]
print("The columns 0 and 1 =\n{}".format(columns_a_b))
print("The data type of the columns is \n{}".format(type(columns_a_b)))

df[3] = df[0] + df[1]
print(df)
df.drop(3, axis=1, inplace=True)
print(df)
df.drop('a', axis=0, inplace=True)
print(df)
print(df.shape)


print(df.loc['b'])

print(df.iloc[1])

print(df.loc['b', 1])

print(df)
print(df.loc[['b', 'c'], [0, 1]])
