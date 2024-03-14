import numpy as np
import pandas as pd


df1 = pd.DataFrame({
    'A': ['AO', 'A1', 'A2', 'A3'], 
    'B': ['BO', 'B1', 'B2', 'B3'],
    'C': ['CO', 'C1', 'C2', 'C3'],
    'D': ['DO', 'D1', 'D2', 'D3'],
    },
    index=np.array([0, 1, 2, 3]))



df2 = pd.DataFrame({                    
     'A': ['A4', 'A5', 'A6', 'A7'],
     'B': ['B4', 'B5', 'B6', 'B7'],
     'C': ['C4', 'C5', 'C6', 'C7'],
     'D': ['D4', 'D5', 'D6', 'D7']
     },
     index=np.array([4, 5, 6, 7]))

                                                                        
df3 = pd.DataFrame({                
      'A': ['A8', 'A9', 'A10', 'A11'],
      'B': ['B8', 'B9', 'B10', 'B11'],
      'C': ['C8', 'C9', 'C10', 'C11'],
      'D': ['D8', 'D9', 'D10', 'D11']
      },
      index=np.array([8, 9, 10, 11]))
print(df1)
print("=" * 100)
print(df2)
print("=" * 100)
print(df3)
print("=" * 100)

conactedArray = pd.concat([df1, df2, df3])
print(conactedArray)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})   

# merge
print(pd.merge(left, right, how='inner',on='key'))

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                   'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left, right, how="right", on=['key1', 'key2']))
print(pd.merge(left, right, how='outer', on=['key1', 'key2']))

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=np.array(['K0', 'K1', 'K2'])) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=np.array(['K0', 'K2', 'K3']))

# joining
print(left.join(right))
