import pandas as pd
import numpy as np

# Tạo Series
ser = pd.Series(np.random.randint(1, 10, 7))

# Tìm vị trí của các số là bội của 3
vi_tri = ser.index[ser % 3 == 0].tolist()

# In kết quả
print("Series ban đầu:")
print(ser)
print("\nVị trí các số là bội của 3:")
print(vi_tri)
