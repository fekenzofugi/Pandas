import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

# declaration
series = pd.Series(data = my_data)
print(series)
series = pd.Series(data = my_data, index = labels)
print(series)

series = pd.Series(arr, labels)
print(series)

# notice that when we pass a dictionary as a parameter the keys are the labels.
series = pd.Series(d)
print(series)

# indexing
ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser2)

print(ser1['USA'])

ser3 = pd.Series(data=labels)
print(ser3)
print(ser3[0])

# when an operation happens the sum will cast the integers to floats(avoinding losing information)
# and the unmatched lables gets assing to a null value.
ser1_plus_ser2 = ser1 + ser2
print(ser1_plus_ser2)
