# What's the difference between a NumPy Array and a Pandas Series?
The main difference is that pandas Series can be accesed by its lable.

# list, NumPy array and dictionary as parameters to a Pandas Series
A python list and a NumPy array have the same behavior when passed as parameters to the constructor
of a Series object.

When a dictionary is passed as an argument, the dictionary keys are the lables of the Series and the 
values are the corresponding data of that Series.

# A series can hold any data type?
Yes, a Pandas Series can hold pretty much every data type, we can even pass a reference to a function.
```
import pandas as pd

series = pd.Series(data = [sum, print, len])
```
