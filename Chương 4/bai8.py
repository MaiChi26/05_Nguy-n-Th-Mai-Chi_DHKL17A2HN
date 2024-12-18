import pandas as pd
import numpy as np

ser = pd.Series(np.random.random(20))
thap_phan = pd.qcut(ser, q=10, labels=[f'Decile {i+1}' for i in range(10)])

print("Series ban đầu:")
print(ser)
print("\nSeries sau khi thay thế bằng tên phân vị:")
print(thap_phan)
