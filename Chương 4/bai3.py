import pandas as pd
import numpy as np

# Input
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.DataFrame({'Column1': ser1, 'Column2': ser2})
print(df)



