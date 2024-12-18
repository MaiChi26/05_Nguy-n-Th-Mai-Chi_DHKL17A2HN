import pandas as pd
import numpy as np

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

value_counts = ser.value_counts()
top2_values = value_counts.nlargest(2).index
ser_modified = ser.where(ser.isin(top2_values), other='Other')

print("Series ban đầu:")
print(ser)
print("\nSeries sau khi thay thế:")
print(ser_modified)
