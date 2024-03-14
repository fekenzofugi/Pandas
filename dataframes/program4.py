import numpy as np
import pandas as pd

d = {'A': [1,2,np.nan], 'B': [5,np.nan,np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

df.dropna() # drop every row with a NaN value

df.dropna(thresh=2) # drop every row with NaN value excluding row 2

df.fillna(inplace=True,value=df['A'].mean())
print(df)


