import pandas as pd
import numpy as np

# Input
mylist = list("abcedfghijklmnopqrstuvwxyz")
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = ser.reset_index()

df.columns = ['Index', 'Value']

print(df)
