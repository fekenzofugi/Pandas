
import numpy as np
import pandas as pd

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
print(outside)
inside = [1, 2, 3, 1, 2, 3]
print(inside)
hier_index = list(zip(outside, inside))
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df = pd.DataFrame(np.random.randn(6,2), hier_index, np.array(['A', 'B']))
print(df)

df.index.names = ['Groups', 'Num']
print(df)

print(df.loc['G2'].loc[2]['B'])

print("=" * 100)
print(df)

print(df.loc['G2'].loc[3]['B'])
